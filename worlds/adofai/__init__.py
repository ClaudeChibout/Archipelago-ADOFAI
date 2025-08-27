# world/__init__.py

from worlds.AutoWorld import World
from BaseClasses import  Item, Location, ItemClassification, Region
from worlds.generic.Rules import add_rule
from Options import OptionError


# Import des données
from .Items import adofai_items, MainWorldsKeys, MainWorldsTutoKeys, OtherItems, XtraWorldsKeys, XtraTutoKeys
from .Items import BWorldKeys, BWorldTutoKeys, CrownWorldsKeys, CrownWorldsTutoKeys, StarWorldsKeys, StarWorldsTutoKeys
from .Items import NeonCosmosWorldsKeys, NeonCosmosWorldsTutoKeys, NeonCosmosWorldsEXKeys, NeonCosmosWorldsEXTutoKeys
from .Locations import adofai_locations, MainWorldsLoc, MainWorldsTutoLoc, XtraWorldsLoc, XtraTutoLoc
from .Locations import BWorldLoc, BWorldTutoLoc, CrownWorldsLoc, CrownWorldsTutoLoc, StarWorldsLoc, StarWorldsTutoLoc
from .Locations import NeonCosmosWorldsLoc, NeonCosmosWorldsTutoLoc, NeonCosmosWorldsEXLoc, NeonCosmosWorldsEXTutoLoc
from .Options import ADOFAIOptions


all_items = adofai_items | MainWorldsKeys | MainWorldsTutoKeys | XtraTutoKeys | XtraWorldsKeys
all_items = all_items | OtherItems | BWorldKeys | BWorldTutoKeys | CrownWorldsKeys | CrownWorldsTutoKeys
all_items = all_items | StarWorldsKeys | StarWorldsTutoKeys
all_items = all_items | NeonCosmosWorldsKeys | NeonCosmosWorldsTutoKeys | NeonCosmosWorldsEXKeys | NeonCosmosWorldsEXTutoKeys
_item_name_to_id = {n: d.id for n, d in all_items.items()}

all_locs = adofai_locations | MainWorldsLoc | MainWorldsTutoLoc | XtraTutoLoc | XtraWorldsLoc
all_locs = all_locs | BWorldLoc | BWorldTutoLoc | CrownWorldsLoc | CrownWorldsTutoLoc
all_locs = all_locs | StarWorldsLoc | StarWorldsTutoLoc 
all_locs = all_locs | NeonCosmosWorldsLoc | NeonCosmosWorldsTutoLoc | NeonCosmosWorldsEXLoc | NeonCosmosWorldsEXTutoLoc
_location_name_to_id = {n: d.id for n, d in all_locs.items()}



class ADOFAIWorld(World):
    game = "A Dance of Fire and Ice"
    topology_present = True

    options_dataclass = ADOFAIOptions
    options: ADOFAIOptions 
    
    item_name_to_id: dict[str, int] = _item_name_to_id
    location_name_to_id: dict[str, int] = _location_name_to_id

    def create_regions(self):
        # Filtre pool effectif selon options
        used_locs = self.get_used_locations()

        # Création des régions et placement des locations filtrées
        menu = Region("Menu", self.player, self.multiworld)

        vLoc = Location(self.player, "Victory", 54125399, menu)
        menu.locations.append(vLoc)
        
        vItem = Item("Victory", ItemClassification.progression, 54125399, self.player)
        self.multiworld.itempool.append(vItem)

        vLoc.place_locked_item(vItem)
        

        self.multiworld.regions.append(menu)


        region_by_name = {"Menu": menu}
        for wname in sorted({data.world for data in used_locs.values() if data.world}):
            region = Region(wname, self.player, self.multiworld)
            self.multiworld.regions.append(region)
            region_by_name[wname] = region
            menu.connect(region)

        for loc_name, loc_data in used_locs.items():
            target = region_by_name.get(loc_data.world or "Menu")
            loc = Location(self.player, loc_name, loc_data.id, target)
            target.locations.append(loc)
            
            # add the rules for locations
            if loc_name not in adofai_locations.keys():
                add_rule(loc, lambda state, ln=loc_name: state.has(f"Key_Level_{ln}", self.player))


    def create_items(self) -> None:
        """Construit l'itempool: progression + useful, puis filler jusqu'à couvrir toutes les locations.
        Je dois utiliser les options pour créer le pool d'item
        """
        self.generate_early()

        def make_item(name: str) -> Item:
            data = all_items[name]
            cls = {
                "progression": ItemClassification.progression,
                "useful": ItemClassification.useful,
                "filler": ItemClassification.filler,
                "trap": ItemClassification.trap,
            }.get(data.classification, ItemClassification.filler)
            return Item(name, cls, data.id, self.player)

        used_items = adofai_items | MainWorldsKeys

        if self.options.main_worlds_tuto.value:
            used_items.update(MainWorldsTutoKeys)
        if self.options.xtra_worlds.value:
            used_items.update(XtraWorldsKeys)
        if self.options.xtra_worlds_tuto.value:
            used_items.update(XtraTutoKeys)
        if self.options.b_world.value:
            used_items.update(BWorldKeys)
        if self.options.b_world_tuto.value:
            used_items.update(BWorldTutoKeys)
        if self.options.crown_worlds.value:
            used_items.update(CrownWorldsKeys)
        if self.options.crown_worlds_tuto.value:
            used_items.update(CrownWorldsTutoKeys)
        if self.options.star_worlds.value:
            used_items.update(StarWorldsKeys)
        if self.options.star_worlds_tuto.value:
            used_items.update(StarWorldsTutoKeys)
        if self.options.neon_cosmos_worlds.value:
            used_items.update(NeonCosmosWorldsKeys)
        if self.options.neon_cosmos_worlds_ex_tuto.value:
            used_items.update(NeonCosmosWorldsTutoKeys)
        if self.options.neon_cosmos_worlds.value:
            used_items.update(NeonCosmosWorldsEXKeys)
        if self.options.neon_cosmos_worlds_ex_tuto.value:
            used_items.update(NeonCosmosWorldsEXTutoKeys)

        for item_name in used_items.keys():
            self.multiworld.itempool.append(make_item(item_name))
        
        total_locations = len([
            loc for loc in self.multiworld.get_locations(self.player)
            if not getattr(loc, "event", False)
        ])
        
        while len([i for i in self.multiworld.itempool if i.player == self.player]) < total_locations:
            filler_name = self.get_filler_item_name()
            filler_data = OtherItems[filler_name]
            self.multiworld.itempool.append(Item(filler_name, ItemClassification.filler, filler_data.id, self.player))


    def set_rules(self) -> None:
        """Tout est ouvert par défaut; ajoute tes règles d'accès par région si besoin."""
        self.world.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
        return

    def get_filler_item_name(self) -> str:
        """Nom du filler par défaut préféré."""
        for name, data in all_items.items():
            if data.classification == "filler":
                return name
        return "Filler Note"

    def fill_slot_data(self) -> dict:
        """Données envoyées au client ADOFAI."""
        return {
            "percentage_goal_completion": int(self.options.percentage_goal_completion.value),
            "completion_goal": self.options.completion_goal.value,
            "goal_levels": str(
                " ".join([x for x in self.get_used_locations().keys() if x.endswith("X")])
            ) if self.options.completion_goal.value == 0 else (
                str(self.options.goal_levels.value) if self.options.completion_goal.value == 1 else
                OptionError("option goal bad value")
            ),


            "world_regions": sorted({data.world for data in adofai_locations.values() if data.world}),
            "death_link": bool(self.options.death_link.value),
            "main_worlds_tuto": bool(self.options.main_worlds_tuto.value),
            "xtra_worlds": bool(self.options.xtra_worlds.value),
            "xtra_worlds_tuto": bool(self.options.xtra_worlds_tuto.value),
            "b_world": bool(self.options.b_world.value),
            "b_world_tuto": bool(self.options.b_world_tuto.value),
            "crown_worlds": bool(self.options.crown_worlds.value),
            "crown_worlds_tuto": bool(self.options.crown_worlds_tuto.value),
            "star_worlds": bool(self.options.star_worlds.value),
            "star_worlds_tuto": bool(self.options.star_worlds_tuto.value),
            "neon_cosmos_worlds": bool(self.options.neon_cosmos_worlds.value),
            "neon_cosmos_worlds_tuto": bool(self.options.neon_cosmos_worlds_tuto.value),
            "neon_cosmos_worlds_ex": bool(self.options.neon_cosmos_worlds_ex.value),
            "neon_cosmos_worlds_ex_tuto": bool(self.options.neon_cosmos_worlds_ex_tuto.value),

        }
    
    def get_used_locations(self):
        used_locs = adofai_locations.copy()
        used_locs.update(MainWorldsLoc)

        if self.options.main_worlds_tuto.value:
            used_locs.update(MainWorldsTutoLoc)
        if self.options.xtra_worlds_tuto.value:
            used_locs.update(XtraTutoLoc)
        if self.options.xtra_worlds.value:
            used_locs.update(XtraWorldsLoc)
        if self.options.b_world.value:
            used_locs.update(BWorldLoc)
        if self.options.b_world_tuto.value:
            used_locs.update(BWorldTutoLoc)
        if self.options.crown_worlds.value:
            used_locs.update(CrownWorldsLoc)
        if self.options.crown_worlds_tuto.value:
            used_locs.update(CrownWorldsTutoLoc)
        if self.options.star_worlds.value:
            used_locs.update(StarWorldsLoc)
        if self.options.star_worlds_tuto.value:
            used_locs.update(StarWorldsTutoLoc)
        if self.options.neon_cosmos_worlds.value:
            used_locs.update(NeonCosmosWorldsLoc)
        if self.options.neon_cosmos_worlds_ex_tuto.value:
            used_locs.update(NeonCosmosWorldsTutoLoc)
        if self.options.neon_cosmos_worlds.value:
            used_locs.update(NeonCosmosWorldsEXLoc)
        if self.options.neon_cosmos_worlds_ex_tuto.value:
            used_locs.update(NeonCosmosWorldsEXTutoLoc)

        return used_locs





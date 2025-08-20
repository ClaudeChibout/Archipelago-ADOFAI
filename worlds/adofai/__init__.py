# world/__init__.py

from worlds.AutoWorld import World
from BaseClasses import  Item, Location, ItemClassification, Region

# Import des données
from .Items import adofai_items, MainWorldsKeys, MainWorldsTutoKeys, OtherItems, XtraWorldsKeys, XtraTutoKeys
from .Locations import adofai_locations, MainWorldsLoc, MainWorldsTutoLoc, XtraWorldsLoc, XtraTutoLoc
from .Options import ADOFAIOptions


class ADOFAIWorld(World):
    game = "A Dance of Fire and Ice"
    topology_present = True

    options_dataclass = ADOFAIOptions
    options: ADOFAIOptions  

    used_adofai_locations = adofai_locations.copy()
    used_adofai_items = adofai_items.copy()

    item_name_to_id: dict[str, int] = {}
    location_name_to_id: dict[str, int] = {}

    def generate_early(self):
        super().generate_early()

        self.used_adofai_locations.update(MainWorldsLoc)
        self.used_adofai_locations.update(MainWorldsTutoLoc if bool(self.options.main_worlds_tuto.value) else {})
        self.used_adofai_locations.update(XtraTutoLoc if bool(self.options.xtra_worlds_tuto.value) else {})
        self.used_adofai_locations.update(XtraWorldsLoc if bool(self.options.xtra_worlds.value) else {})

        self.used_adofai_items.update(MainWorldsKeys)
        self.used_adofai_items.update(MainWorldsTutoKeys if bool(self.options.main_worlds_tuto.value) else {})
        self.used_adofai_items.update(XtraTutoKeys if bool(self.options.xtra_worlds_tuto.value) else {})
        self.used_adofai_items.update(XtraWorldsKeys if bool(self.options.xtra_worlds.value) else {})

        self.used_adofai_items.update(OtherItems)

        self.item_name_to_id = {name: data.id for name, data in self.used_adofai_items.items()}
        self.location_name_to_id= {name: data.id for name, data in self.used_adofai_locations.items()}


    def create_regions(self) -> None:
        """Crée 'Menu' + 1 région par monde et y place les locations."""

        # Création de la région 'Menu'
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        

        # Régions par 'world' déclaré dans les locations
        region_by_name: dict[str, Region] = {"Menu": menu}
        world_names = sorted({data.world for data in self.used_adofai_locations.values() if data.world})
        for wname in world_names:
            region = Region(wname, self.player, self.multiworld)
            self.multiworld.regions.append(region)
            region_by_name[wname] = region
            menu.connect(region)

        # Placement des locations dans leur région cible 
        for loc_name, loc_data in self.used_adofai_locations.items():
            target = region_by_name.get(loc_data.world or "Menu")
            location = Location(self.player, loc_name, loc_data.id, target)
            target.locations.append(location)

    def create_items(self) -> None:
        """Construit l'itempool: progression + useful, puis filler jusqu'à couvrir toutes les locations."""
        self.generate_early()

        def make_item(name: str) -> Item:
            data = self.used_adofai_items[name]
            cls = {
                "progression": ItemClassification.progression,
                "useful": ItemClassification.useful,
                "filler": ItemClassification.filler,
                "trap": ItemClassification.trap,
            }.get(data.classification, ItemClassification.filler)
            return Item(name, cls, data.id, self.player)

        progress = [n for n, d in self.used_adofai_items.items() if d.classification == "progression"]
        useful = [n for n, d in self.used_adofai_items.items() if d.classification == "useful"]
        fillers = [n for n, d in self.used_adofai_items.items() if d.classification == "filler"]

        for name in progress + useful:
            self.multiworld.itempool.append(make_item(name))

        total_locations = len(self.location_name_to_id)
        if not fillers:
            fillers = ["Filler Note"]

        while len(self.multiworld.itempool) < total_locations:
            fname = fillers[0]
            if fname in self.used_adofai_items:
                self.multiworld.itempool.append(make_item(fname))
            else:
                self.multiworld.itempool.append(Item(fname, ItemClassification.filler, -1, self.player))

    def set_rules(self) -> None:
        """Tout est ouvert par défaut; ajoute tes règles d'accès par région si besoin."""
        return

    def get_filler_item_name(self) -> str:
        """Nom du filler par défaut préféré."""
        for name, data in self.used_adofai_items.items():
            if data.classification == "filler":
                return name
        return "Filler Note"

    def fill_slot_data(self) -> dict:
        """Données envoyées au client ADOFAI."""
        return {
            "goal": "clear_some_worlds",
            "death_link": bool(self.options.death_link.value),
            "main_worlds_tuto": bool(self.options.main_worlds_tuto.value),
            "xtra_worlds": bool(self.options.xtra_worlds.value),
            "xtra_worlds_tuto": bool(self.options.xtra_worlds_tuto.value)
        }
    






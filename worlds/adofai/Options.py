from Options import Toggle, PerGameCommonOptions
from dataclasses import dataclass
class DeathLink(Toggle):
    display_name = "DeathLink"

class MainWorldsTuto(Toggle):
    display_name = "MainWorldsTuto"

class XtraWorlds(Toggle):
    display_name = "XtraWorlds"

class XtraWorldsTuto(Toggle):
    display_name = "XtraWorldsTuto"


@dataclass
class ADOFAIOptions(PerGameCommonOptions):
    death_link: DeathLink
    main_worlds_tuto: MainWorldsTuto
    xtra_worlds: XtraWorlds
    xtra_worlds_tuto: XtraWorldsTuto
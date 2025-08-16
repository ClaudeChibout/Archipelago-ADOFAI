from Options import Toggle, PerGameCommonOptions
from dataclasses import dataclass
class DeathLink(Toggle):
    display_name = "DeathLink"

@dataclass
class ADOFAIOptions(PerGameCommonOptions):
    death_link: DeathLink
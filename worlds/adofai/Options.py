from Options import Toggle, PerGameCommonOptions, Choice, Range, FreeText
from dataclasses import dataclass
class DeathLink(Toggle):
    display_name = "DeathLink"

class MainWorldsTuto(Toggle):
    display_name = "MainWorldsTuto"

class XtraWorlds(Toggle):
    display_name = "XtraWorlds"

class XtraWorldsTuto(Toggle):
    display_name = "XtraWorldsTuto"

class BWorld(Toggle):
    display_name = "BWorld"

class BWorldTuto(Toggle):
    display_name = "BWorldTuto"

class CrownWorlds(Toggle):
    display_name= "CronwWorlds"

class CrownWorldsTuto(Toggle):
    display_name= "CronwWorldsTuto"

class StarWorlds(Toggle):
    display_name= "StarWorlds"

class StarWorldsTuto(Toggle):
    display_name= "StarWorldsTuto"

class NeonCosmosWorlds(Toggle):
    display_name= "NeonCosmosWorlds"

class NeonCosmosWorldsTuto(Toggle):
    display_name= "NeonCosmosWorldsTuto"

class NeonCosmosWorldsEX(Toggle):
    display_name= "NeonCosmosWorldsEX"

class NeonCosmosWorldsEXTuto(Toggle):
    display_name= "NeonCosmosWorldsEXTuto"

class AprilFoolsWorlds(Toggle):
    display_name= "AprilFoolsWorlds"

class CompletionGoal(Choice):
    display_name = "CompletionGoal"
    option_allX = 0
    option_goalLevels = 1
    default = 0 

class PercentageGoalCompletion(Range):
    display_name = "PercentageGoalCompletion"
    range_start = 0
    range_end = 100
    default = 80

class GoalLevels(FreeText):
    display_name="GoalLevels"


@dataclass
class ADOFAIOptions(PerGameCommonOptions):
    death_link: DeathLink
    main_worlds_tuto: MainWorldsTuto
    xtra_worlds: XtraWorlds
    xtra_worlds_tuto: XtraWorldsTuto
    b_world: BWorld
    b_world_tuto: BWorldTuto
    crown_worlds: CrownWorlds
    crown_worlds_tuto: CrownWorldsTuto
    star_worlds: StarWorlds
    star_worlds_tuto: StarWorldsTuto
    neon_cosmos_worlds: NeonCosmosWorlds
    neon_cosmos_worlds_tuto: NeonCosmosWorldsTuto
    neon_cosmos_worlds_ex: NeonCosmosWorldsEX
    neon_cosmos_worlds_ex_tuto: NeonCosmosWorldsEXTuto
    april_fools_worlds: AprilFoolsWorlds
    percentage_goal_completion: PercentageGoalCompletion
    completion_goal: CompletionGoal
    goal_levels: GoalLevels
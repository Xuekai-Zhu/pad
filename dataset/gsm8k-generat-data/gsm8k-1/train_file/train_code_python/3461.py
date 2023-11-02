def solution():
    """After complaints from the residents of Tatoosh about the number of cats on the island, the wildlife service carried out a relocation mission that saw the number of cats on the island drastically reduced. On the first relocation mission, 600 cats were relocated from the island to a neighboring island. On the second mission, half of the remaining cats were relocated to a rescue center inland. If the number of cats originally on the island was 1800, how many cats remained on the island after the rescue mission?"""
    initial_cats = 1800
    first_mission_cats = 600
    remaining_cats = initial_cats - first_mission_cats
    second_mission_cats = remaining_cats / 2
    cats_on_island_after_missions = remaining_cats - second_mission_cats
    result = cats_on_island_after_missions
    return result

print(solution())
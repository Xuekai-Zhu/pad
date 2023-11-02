def solution():
    """Mary is an avid gardener. Yesterday, she received 18 new potted plants from her favorite plant nursery. She already has 2 potted plants on each of the 40 window ledges of her large country home. Feeling generous, she has decided that she will give 1 potted plant from each ledge to friends and family tomorrow. How many potted plants will Mary remain with?"""
    new_plants = 18
    total_ledges = 40
    plants_per_ledge = 2
    plants_given_away = total_ledges * 1
    total_plants = new_plants + (total_ledges * plants_per_ledge)
    remaining_plants = total_plants - plants_given_away
    result = remaining_plants
    return result

print(solution())
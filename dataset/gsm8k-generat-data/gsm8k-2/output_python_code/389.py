def solution():
    """Oscar wants to train for a marathon. He plans to add 2/3 of a mile each week until he reaches a 20-mile run. How many weeks before the marathon should he start training if he has already run 2 miles?"""
    starting_distance = 2
    target_distance = 20
    distance_increase_per_week = 2/3
    total_distance_to_add = target_distance - starting_distance
    weeks_needed = total_distance_to_add / distance_increase_per_week
    result = weeks_needed
    return result

print(solution())
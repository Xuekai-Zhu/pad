def solution():
    """A bear is hunting for her cubs and herself. She needs 210 pounds of meat in a week. Each cub needs 35 pounds a week and she has 4 cubs. She hunts rabbits, which are five pounds each. If she hunts daily, how many rabbits does she need to catch each day?"""
    total_meat_needed = 210
    cub_meat_per_week = 35
    num_cubs = 4
    bear_meat_per_week = total_meat_needed - (cub_meat_per_week * num_cubs)
    rabbits_needed_per_day = (bear_meat_per_week / 7) / 5
    result = rabbits_needed_per_day
    return result

print(solution())
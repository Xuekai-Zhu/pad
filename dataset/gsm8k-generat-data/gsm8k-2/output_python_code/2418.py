def solution():
    """A bear is hunting for her cubs and herself. She needs 210 pounds of meat in a week. Each cub needs 35 pounds a week and she has 4 cubs. She hunts rabbits, which are five pounds each. If she hunts daily, how many rabbits does she need to catch each day?"""
    weekly_cub_food = 35 * 4
    weekly_bear_food = 210 - weekly_cub_food
    daily_bear_food = weekly_bear_food / 7
    rabbits_per_day = daily_bear_food / 5
    result = rabbits_per_day
    return result

print(solution())
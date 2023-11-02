def solution():
    """Sandy's goal is to drink 3 liters of water in a day. She drinks 500 milliliters of water every after 2 hours. After how many hours will she be able to drink a total of 3 liters of water?"""
    goal_in_liters = 3
    water_per_drink = 0.5
    drinks_needed = goal_in_liters / water_per_drink
    time_between_drinks = 2
    total_time = (drinks_needed - 1) * time_between_drinks
    result = total_time
    return result

print(solution())
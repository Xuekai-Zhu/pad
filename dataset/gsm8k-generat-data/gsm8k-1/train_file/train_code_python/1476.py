def solution():
    """Jack goes hunting 6 times a month. The hunting season lasts for 1 quarter of the year. He catches 2 deers each time he goes hunting and they weigh 600 pounds each. He keeps half the weight of deer a year. How much deer does he keep in pounds?"""
    hunting_frequency = 6
    deer_caught_each_time = 2
    weight_of_each_deer = 600
    season_length_in_months = 3
    total_hunts_in_season = hunting_frequency * season_length_in_months
    total_deer_caught_in_season = total_hunts_in_season * deer_caught_each_time
    total_weight_of_deer_caught_in_season = total_deer_caught_in_season * weight_of_each_deer
    weight_of_deer_kept = total_weight_of_deer_caught_in_season / 2
    result = weight_of_deer_kept
    return result

print(solution())
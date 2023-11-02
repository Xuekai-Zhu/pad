def solution():
    """Jack goes hunting 6 times a month. The hunting season lasts for 1 quarter of the year. He catches 2 deers each time he goes hunting and they weigh 600 pounds each. He keeps half the weight of deer a year. How much deer does he keep in pounds?"""
    hunting_per_month = 6
    hunting_season = 0.25  # as a decimal
    deers_caught_per_hunting = 2
    deer_weight = 600
    total_deer_caught = hunting_per_month * 12 * hunting_season * deers_caught_per_hunting
    total_weight = total_deer_caught * deer_weight
    weight_kept = total_weight / 2
    result = weight_kept
    return result

print(solution())
def solution():
    """When the water is cold Ray swims a mile in 16 minutes. When the water is warm Ray swims a mile in 2 minutes more than twice as long. How much longer does Ray take to swim 3 miles on a hot day than a cold day?"""
    cold_water_time = 16
    warm_water_time = 2 * cold_water_time + 2
    cold_water_total = 3 * cold_water_time
    warm_water_total = 3 * warm_water_time
    time_difference = warm_water_total - cold_water_total
    result = time_difference
    return result

print(solution())
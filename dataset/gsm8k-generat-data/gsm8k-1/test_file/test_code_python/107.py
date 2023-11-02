def solution():
    """Julia’s boat sprang a leak while she was out on the lake. The boat was taking on two liters of water for every ten feet she rowed back towards shore. It took her sixteen seconds to row twenty feet. The shore was 64 seconds away. How much water had the boat taken on by the time Julia reached shore?"""
    water_per_feet = 2 / 10
    distance_to_shore = 64 / 16 * 20
    water_taken_on = water_per_feet * distance_to_shore
    result = water_taken_on
    return result

print(solution())
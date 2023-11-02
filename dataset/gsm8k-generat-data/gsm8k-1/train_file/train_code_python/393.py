def solution():
    """Chad sandwiches 2 crackers with a scoop of peanut butter. He has 5 of these crackers a night before bed. A box of crackers has 4 sleeves with each sleeve holding 28 crackers. How many nights will 5 boxes of crackers last him?"""
    crackers_per_sleeve = 28
    sleeves_per_box = 4
    crackers_per_box = crackers_per_sleeve * sleeves_per_box
    boxes_of_crackers = 5
    crackers_per_night = 5 * 2
    nights_per_box = crackers_per_box / crackers_per_night
    total_nights = nights_per_box * boxes_of_crackers
    result = total_nights
    return result

print(solution())
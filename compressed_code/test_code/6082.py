def solution():
    
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
def solution():
    crackers_per_sleeve = 28
    sleeves_per_box = 4
    boxes = 5

    # Calculate the total number of crackers for 5 boxes
    total_crackers = crackers_per_sleeve * sleeves_per_box * boxes

    # Calculate the number of nights the crackers will last
    crackers_per_night = 5  # 5 sandwiches per night
    num_nights = total_crackers / (2 * crackers_per_night)  # 2 crackers per sandwich
    result = num_nights
    return result

print(solution())
def solution():
    crackers_per_sleeve = 28  # Each sleeve of crackers has 28 crackers
    sleeves_per_box = 4  # Each box of crackers has 4 sleeves
    crackers_per_sandwich = 2  # Chad sandwiches 2 crackers with peanut butter
    sandwiches_per_night = 5  # Chad eats 5 crackers sandwiches per night
    number_of_boxes = 5  # Chad has 5 boxes of crackers

    # Calculate the total number of crackers in 5 boxes
    total_crackers = crackers_per_sleeve * sleeves_per_box * number_of_boxes

    # Calculate the number of nights 5 boxes will last Chad
    nights = total_crackers // (crackers_per_sandwich * sandwiches_per_night)
    result = nights
    return result

print(solution())
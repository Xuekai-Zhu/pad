def solution():
    # Find the total number of crackers in 5 boxes
    crackers_per_box = 4 * 28  # Each box has 4 sleeves with 28 crackers per sleeve
    total_crackers = crackers_per_box * 5

    # Find how many nights 5 boxes of crackers will last
    crackers_per_sandwich = 2
    sandwiches_per_night = 5
    nights = total_crackers // (crackers_per_sandwich * sandwiches_per_night)

    result = nights
    return result

print(solution())
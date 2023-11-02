def solution():
    """Chad sandwiches 2 crackers with a scoop of peanut butter. He has 5 of these crackers a night before bed. A box of crackers has 4 sleeves with each sleeve holding 28 crackers. How many nights will 5 boxes of crackers last him?"""
    # Define the number of crackers per night and per box
    crackers_per_night = 5 * 2
    crackers_per_box = 4 * 28

    # Calculate the total number of crackers in 5 boxes
    total_crackers = 5 * crackers_per_box

    # Calculate the number of nights the crackers will last
    nights = total_crackers // crackers_per_night

    # return the result
    result = nights
    return result

print(solution())
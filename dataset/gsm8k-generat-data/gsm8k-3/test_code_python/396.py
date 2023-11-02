def solution():
    """Chad sandwiches 2 crackers with a scoop of peanut butter.  He has 5 of these crackers a night before bed.  A box of crackers has 4 sleeves with each sleeve holding 28 crackers.  How many nights will 5 boxes of crackers last him?"""
    # Define the number of crackers per sandwich
    crackers_per_sandwich = 2

    # Define the number of sandwiches per night
    sandwiches_per_night = 5

    # Calculate the number of crackers Chad eats per night
    crackers_per_night = crackers_per_sandwich * sandwiches_per_night

    # Define the number of boxes of crackers
    num_boxes = 5

    # Define the number of sleeves per box
    num_sleeves_per_box = 4

    # Define the number of crackers per sleeve
    num_crackers_per_sleeve = 28

    # Calculate the total number of crackers
    total_crackers = num_boxes * num_sleeves_per_box * num_crackers_per_sleeve

    # Calculate the number of nights the crackers will last
    nights_last = total_crackers // crackers_per_night

    # Display the number of nights
    result = nights_last
    return result

print(solution())
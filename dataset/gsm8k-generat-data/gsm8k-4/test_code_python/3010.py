def solution():
    """Jon's laundry machine can do 5 pounds of laundry at a time.  4 shirts weigh 1 pound and 2 pairs of pants weigh 1 pound.
     If he needs to wash 20 shirts and 20 pants, how many loads of laundry does he have to do?"""
    # Define the weight of 4 shirts and 2 pants
    weight_of_4_shirts_2_pants = 1

    # Calculate the total weight of washing 20 shirts and 20 pants
    total_weight = (20 * 4 / weight_of_4_shirts_2_pants) + (20 * 2 / weight_of_4_shirts_2_pants)

    # Calculate the number of loads needed, rounding up to the nearest integer
    loads_needed = int(total_weight / 5) + (total_weight % 5 > 0)

    result = loads_needed
    return result

print(solution())
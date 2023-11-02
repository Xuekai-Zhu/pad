def solution():
    """Jon's laundry machine can do 5 pounds of laundry at a time.  4 shirts weigh 1 pound and 2 pairs of pants weigh 1 pound.  If he needs to wash 20 shirts and 20 pants, how many loads of laundry does he have to do?"""
    # Calculate the total weight of the shirts and pants
    total_weight = (20 / 4) + (20 / 2)

    # Calculate the number of loads required
    loads = total_weight / 5

    # Round up to the nearest whole number
    loads = math.ceil(loads)

    # Display the number of loads required
    result = loads
    return result

print(solution())
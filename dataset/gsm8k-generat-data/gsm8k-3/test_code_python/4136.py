def solution():
    """Mary uses plastic grocery bags that can hold a maximum of twenty pounds. She buys 4 pounds of green beans, 6 pounds milk, and twice the amount of carrots as green beans. How many more pounds of groceries can Mary fit in that bag?"""
    # Define the maximum weight the bag can hold
    MAX_WEIGHT = 20

    # Calculate the total weight of the items Mary bought
    total_weight = 4 + 6 + (2 * 4)  # twice the weight of green beans

    # Calculate the remaining weight Mary can fit in the bag
    remaining_weight = MAX_WEIGHT - total_weight

    # Display the remaining weight Mary can fit in the bag
    result = remaining_weight
    return result

print(solution())
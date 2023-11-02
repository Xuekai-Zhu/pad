def solution():
    """There are 1250 pairs of shoes in the warehouse. There are 540 pairs that are blue. The rest are either green or purple. The number of green shoes is equal to the number of purple shoes. How many pairs of purple shoes are in the warehouse?"""
    # Define the total number of shoes and the number of blue shoes
    total_shoes = 1250
    blue_shoes = 540

    # Calculate the number of green shoes
    green_shoes = (total_shoes - blue_shoes) / 2

    # Calculate the number of purple shoes
    purple_shoes = green_shoes

    # Return the result
    result = purple_shoes
    return result

print(solution())
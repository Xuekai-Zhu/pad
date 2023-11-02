def solution():
    """There are 1250 pairs of shoes in the warehouse. There are 540 pairs that are blue. The rest are either green or purple. The number of green shoes is equal to the number of purple shoes. How many pairs of purple shoes are in the warehouse?"""
    # Define the number of blue shoes
    blue_shoes = 540

    # Calculate the number of non-blue shoes
    non_blue_shoes = 1250 - blue_shoes

    # Calculate the number of green shoes
    green_shoes = non_blue_shoes / 2
    
    # Calculate the number of purple shoes
    purple_shoes = green_shoes

    # Display the number of purple shoes
    result = purple_shoes
    return result

print(solution())
def solution():
    
    # Define the initial size of the land
    land_size = 80

    # Calculate the size of the land sold for $50
    land_sold_50 = land_size / 2

    # Calculate the size of the land sold for $30
    land_sold_30 = land_size / 4

    # Calculate the size of the land remaining after selling for $30
    land_remaining = land_size - land_sold_50 - land_sold_30

    # Calculate the total earnings from selling the land
    total_earnings = land_sold_30 * 3

    # return the result
    result = total_earnings
    return result

print(solution())
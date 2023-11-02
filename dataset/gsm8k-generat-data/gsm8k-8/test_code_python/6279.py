def solution():
    # Define the prices of the birdhouses
    large_price = 22
    medium_price = 16
    small_price = 7

    # Define the number of birdhouses sold
    num_large = 2
    num_medium = 2
    num_small = 3

    # Calculate the total money made
    total_money = (num_large * large_price) + (num_medium * medium_price) + (num_small * small_price)
    
    result = total_money
    return result

print(solution())
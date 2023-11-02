def solution():
    # Define the number of dozens Maria wants to buy
    dozens = 3

    # Calculate the total number of flowers Maria will get, including the free ones
    total_flowers = dozens * 12 + (dozens // 1) * 2

    # Return the total number of flowers
    result = total_flowers
    return result

print(solution())
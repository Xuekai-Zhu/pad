def solution():
    # Define the number of rolls Nellie has already sold
    rolls_sold = 1 + 10 + 6

    # Calculate the number of rolls Nellie still needs to sell
    rolls_remaining = 45 - rolls_sold
    result = rolls_remaining
    return result

print(solution())
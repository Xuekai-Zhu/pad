def solution():
    # Calculate the number of rolls Chandler has already sold
    sold_rolls = 3 + 4 + 3

    # Calculate the number of rolls Chandler still needs to sell
    remaining_rolls = 12 - sold_rolls
    result = remaining_rolls
    return result

print(solution())
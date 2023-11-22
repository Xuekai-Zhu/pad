def solution():
    
    # Define the initial amount of root beer
    initial_amount = 24

    # Subtract the amount drinked on the first day
    remaining_amount = initial_amount - 4

    # Subtract the amount spilled on the second day
    remaining_amount -= 7

    # return the result
    result = remaining_amount
    return result

print(solution())
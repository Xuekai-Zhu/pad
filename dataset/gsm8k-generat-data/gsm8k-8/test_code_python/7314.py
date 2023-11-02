def solution():
    # Calculate the total number of fries the chef can make
    total_fries = 25 * 15

    # Calculate the number of fries needed
    fries_needed = 200

    # Calculate the number of potatoes used
    potatoes_used = fries_needed / 25

    # Calculate the number of leftover potatoes
    leftover_potatoes = 15 - potatoes_used
    
    result = leftover_potatoes
    return result

print(solution())
def solution():
    # Calculate the number of pennies Iain wants to get rid of
    older_pennies = 30

    # Calculate the remaining pennies after removing the older ones
    remaining_pennies = 200 - older_pennies

    # Calculate the number of pennies to throw out
    throw_out_pennies = 0.2 * remaining_pennies

    # Calculate the final number of pennies Iain will have
    final_pennies = remaining_pennies - throw_out_pennies
    
    result = final_pennies
    return result

print(solution())
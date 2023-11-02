def solution():
    total_pennies = 200
    older_pennies = 30

    # Calculate the number of pennies to be thrown out
    throw_out = int((total_pennies - older_pennies) * 0.2)

    # Calculate the number of pennies Iain will have left
    remaining_pennies = total_pennies - older_pennies - throw_out
    result = remaining_pennies
    return result

print(solution())
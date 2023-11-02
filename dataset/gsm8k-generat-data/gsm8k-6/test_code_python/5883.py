def solution():
    # Calculate the number of pennies that Iain wants to get rid of
    older_pennies = 30

    # Calculate the number of pennies that Iain wants to keep
    remaining_pennies = 200 - older_pennies

    # Calculate the number of pennies that Iain will throw out
    thrown_pennies = 0.20 * remaining_pennies

    # Calculate the number of pennies that Iain will have left
    final_pennies = int(remaining_pennies - thrown_pennies)

    result = final_pennies
    return result

print(solution())
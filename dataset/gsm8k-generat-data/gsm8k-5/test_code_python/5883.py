def solution():
    total_pennies = 200  # Iain has 200 pennies
    older_pennies = 30  # 30 of Iain's pennies are older than he is
    remaining_pennies = total_pennies - older_pennies  # Iain gets rid of the older pennies
    to_be_thrown = int(0.2 * remaining_pennies)  # Iain throws out 20% of his remaining pennies

    # Calculate how many pennies Iain will have left
    pennies_left = remaining_pennies - to_be_thrown
    result = pennies_left
    return result

print(solution())
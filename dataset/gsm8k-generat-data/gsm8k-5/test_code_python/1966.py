def solution():
    # Calculate the total amount of money Selina earned from selling her clothes
    money_earned = (3 * 5) + (5 * 3) + (4 * x)  # x is the number of shirts she sold

    # Subtract the cost of the 2 shirts she bought from her earnings
    money_earned -= 2 * 10

    # Check if the resulting amount equals $30
    if money_earned == 30:
        result = x  # The number of shirts Selina sold
    else:
        result = "Cannot be determined"  # There is no solution that meets the given conditions
    return result

print(solution())
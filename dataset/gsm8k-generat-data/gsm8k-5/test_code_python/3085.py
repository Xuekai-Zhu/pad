def solution():
    pennies = 120  # Caden has 120 pennies
    nickels = 3 * pennies  # Caden has three times as many pennies as nickels
    dimes = nickels / 5  # Caden has five times as many nickels as dimes
    quarters = 2 * dimes  # Caden has twice as many quarters as dimes

    # Calculate the total value of the coins
    total_value = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25)

    result = round(total_value, 2)  # Round to two decimal places
    return result

print(solution())
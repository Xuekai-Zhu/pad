def solution():
    # Calculate the money Simon makes
    simon_money = 30 * 0.5  # Simon sells each red stamp for 50 cents

    # Calculate the money Peter makes
    peter_money = 80 * 0.2  # Peter sells each white stamp for 20 cents

    # Calculate the difference in the amount of money they make
    money_difference = (peter_money - simon_money) / 100  # Convert cents to dollars
    result = money_difference
    return result

print(solution())
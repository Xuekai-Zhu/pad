def solution():
    """Kyle has $12 less than 3 times what Dave has. Kyle then spends a third of it going snowboarding. If Dave has $46, how much money does Kyle have?"""
    # Define Dave's amount of money
    dave_money = 46

    # Calculate Kyle's amount of money
    kyle_money = 3 * dave_money - 12

    # Calculate the amount of money Kyle spends on snowboarding
    snowboarding_cost = kyle_money / 3

    # Calculate Kyle's remaining amount of money
    remaining_money = kyle_money - snowboarding_cost

    # Display Kyle's remaining amount of money
    result = remaining_money
    return result

print(solution())
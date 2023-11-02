def solution():
    """Kyle has $12 less than 3 times what Dave has. Kyle then spends a third of it going snowboarding. If Dave has $46, how much money does Kyle have?"""
    # Define Dave's money
    dave_money = 46

    # Calculate Kyle's money based on Dave's money
    kyle_money = 3 * dave_money - 12

    # Calculate the amount Kyle spends on snowboarding
    snowboarding_cost = kyle_money / 3

    # Subtract the snowboarding cost from Kyle's money
    kyle_money -= snowboarding_cost

    # return the result
    result = kyle_money
    return result

print(solution())
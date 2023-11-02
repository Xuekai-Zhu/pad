def solution():
    dave_money = 46

    # Calculate how much money Kyle has
    kyle_money = 3 * dave_money - 12

    # Calculate how much Kyle spends on snowboarding
    snowboarding_spending = kyle_money / 3

    # Calculate how much money Kyle has left after snowboarding
    kyle_money_left = kyle_money - snowboarding_spending

    result = kyle_money_left
    return result

print(solution())
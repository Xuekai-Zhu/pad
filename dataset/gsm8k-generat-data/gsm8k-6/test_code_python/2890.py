def solution():
    # Calculate how much money Kyle has
    dave_money = 46
    kyle_money = 3 * dave_money - 12  # Kyle has $12 less than 3 times what Dave has
    kyle_money_spent = kyle_money / 3   # Kyle spends a third of his money going snowboarding
    kyle_money_left = kyle_money - kyle_money_spent   # Kyle's remaining money
    result = kyle_money_left
    return result

print(solution())
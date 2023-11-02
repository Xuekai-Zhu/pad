def solution():
    dave_money = 46  # Dave has $46
    kyle_money = 3 * dave_money - 12  # Kyle has $12 less than 3 times what Dave has
    snowboarding_cost = kyle_money / 3  # Kyle spends a third of his money on snowboarding
    kyle_money -= snowboarding_cost  # Subtract the snowboarding cost from Kyle's remaining money
    result = kyle_money
    return result

print(solution())
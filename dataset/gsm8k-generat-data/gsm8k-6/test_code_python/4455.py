def solution():
    # Let x be the initial amount of money
    # Abigail spent 60% of x on food
    food_expense = 0.6 * x
    # The remainder is 40% of x
    remaining_money1 = 0.4 * x
    # Abigail spent 25% of the remainder on her phone bill
    phone_expense = 0.25 * remaining_money1
    # The remaining money after phone bill is spent is the sum of the remaining_money1 and phone_expense
    remaining_money2 = remaining_money1 - phone_expense
    # Abigail spent $20 on entertainment
    remaining_money3 = remaining_money2 - 20
    # The remaining money is $40
    remaining_money4 = 40
    # Solve for x
    x = (remaining_money4 + 20 + phone_expense + food_expense) / 0.15
    result = x
    return result

print(solution())
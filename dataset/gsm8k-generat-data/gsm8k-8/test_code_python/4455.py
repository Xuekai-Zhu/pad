def solution():
    # Define the variables
    initial_money = 0
    food_spending = 0
    remaining_money = 0
    phone_spending = 0

    # Use algebra to solve for initial money
    # Let x be the initial money
    # 60% of x is spent on food, so 0.6x = food_spending
    # The remainder is 40% of x, so 0.4x = remaining_money
    # 25% of remaining_money is spent on the phone bill, so 0.25(0.4x) = phone_spending
    # After spending $20 on entertainment, Abigail is left with $40, so x - food_spending - phone_spending - 20 = 40
    # Simplifying and solving for x, we get x = $200
    initial_money = 200
    return initial_money

print(solution())
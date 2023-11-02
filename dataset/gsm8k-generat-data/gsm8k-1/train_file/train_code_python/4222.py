def solution():
    """Marcia wants to buy some fruit. Apples cost $2, bananas cost $1, and oranges cost $3. If Marcia buys 12 apples, 4 bananas and 4 oranges, what is the average cost of each piece of fruit in dollars?"""
    apple_cost = 2
    banana_cost = 1
    orange_cost = 3
    num_apples = 12
    num_bananas = 4
    num_oranges = 4
    total_cost = (apple_cost * num_apples) + (banana_cost * num_bananas) + (orange_cost * num_oranges)
    num_fruit = num_apples + num_bananas + num_oranges
    avg_cost = total_cost / num_fruit
    result = avg_cost
    return result

print(solution())
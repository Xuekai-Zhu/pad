def solution():
    """Rihanna has $50 to go to the supermarket. Rihanna bought 6 mangoes and 6 cartons of apple juice. Each mango cost $3 and each carton of apple juice cost $3. How much money does Rihanna have left?"""
    money_available = 50
    mangoes_bought = 6
    apple_juice_bought = 6
    mango_cost = 3
    juice_cost = 3
    total_cost = (mangoes_bought * mango_cost) + (apple_juice_bought * juice_cost)
    money_left = money_available - total_cost
    result = money_left
    return result

print(solution())
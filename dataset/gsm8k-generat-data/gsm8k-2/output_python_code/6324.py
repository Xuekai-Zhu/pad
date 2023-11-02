def solution():
    """Rihanna has $50 to go to the supermarket. Rihanna bought 6 mangoes and 6 cartons of apple juice. Each mango cost $3 and each carton of apple juice cost $3. How much money does Rihanna have left?"""
    mango_price = 3
    juice_price = 3
    num_mangoes = 6
    num_juice = 6
    total_cost = (mango_price * num_mangoes) + (juice_price * num_juice)
    remaining_money = 50 - total_cost
    result = remaining_money
    return result

print(solution())
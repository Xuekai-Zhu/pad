def solution():
    """Ursula went to the store and bought butter, bread, a package of cheese, and tea. The bread was 2 times cheaper than the butter, while the price of the butter was 80% of the price of cheese. Tea was the most expensive and cost twice the price of a package of cheese. If the tea cost $10, how much did Ursula pay for her purchases?"""
    tea_cost = 10
    cheese_cost = tea_cost / 2
    butter_cost = cheese_cost * 0.8
    bread_cost = butter_cost / 2
    total_cost = tea_cost + cheese_cost + butter_cost + bread_cost
    result = total_cost
    return result

print(solution())
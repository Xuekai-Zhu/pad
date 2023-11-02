def solution():
    """Mulan has $40. Her father gave her $100. She buys two pairs of jeans at $30 each and a bag for $20. How much money does Mulan have left?"""
    starting_money = 40 + 100
    jeans_cost = 30 * 2
    bag_cost = 20
    total_spent = jeans_cost + bag_cost
    money_left = starting_money - total_spent
    result = money_left
    return result

print(solution())
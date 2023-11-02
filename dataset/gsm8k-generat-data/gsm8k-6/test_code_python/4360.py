def solution():
    tea_cost = 10  # cost of tea

    cheese_cost = tea_cost / 2  # cost of cheese is half the cost of tea

    butter_cost = (80/100) * (2 * cheese_cost)  # cost of butter is 80% of the cost of cheese times 2 (since bread is 2 times cheaper)

    bread_cost = 2 * butter_cost / 2  # cost of bread is 2 times cheaper than butter

    total_cost = tea_cost + cheese_cost + butter_cost + bread_cost  # total cost of all items

    result = total_cost
    return result

print(solution())
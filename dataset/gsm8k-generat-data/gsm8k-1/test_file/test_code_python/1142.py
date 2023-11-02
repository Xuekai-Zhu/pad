def solution():
    """Adam has $100 and wants to spend it to open a rock stand. He can buy rocks for $5 each and sell them for $7 each. If he invests all his money in the rock stand but only sells 60% of his inventory, how much money does he lose?"""
    initial_investment = 100
    rock_cost = 5
    rock_price = 7
    num_rocks = initial_investment // rock_cost
    total_sales = num_rocks * rock_price * 0.6
    total_cost = num_rocks * rock_cost
    loss = total_cost - total_sales
    result = loss
    return result

print(solution())
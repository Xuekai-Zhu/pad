def solution():
    """Bob bought 2 show dogs for $250.00 each to breed as a side business. The female just had a litter of 6 puppies. If he sells each puppy for $350.00, what is his total profit?"""
    dog_cost = 2 * 250
    puppy_sales = 6 * 350
    total_profit = puppy_sales - dog_cost
    result = total_profit
    return result

print(solution())
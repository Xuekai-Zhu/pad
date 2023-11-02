def solution():
    """Prudence was starting a cupcake business. She figured that each cupcake cost $0.75 to make. The first 2 dozen that she made burnt and she had to throw them out. The next 2 came out perfectly and she ended up eating 5 cupcakes right away. Later that day she made 2 more dozen cupcakes and decided to eat 4 more. If she sells the remaining cupcakes at $2.00 each, how much is her net profit?"""
    cost_per_cupcake = 0.75
    cupcakes_burnt = 2 * 12
    cupcakes_perfect = 2 * 12
    cupcakes_eaten = 5 + 4
    cupcakes_remaining = (cupcakes_perfect + cupcakes_burnt) - cupcakes_eaten
    revenue = cupcakes_remaining * 2
    cost = (cupcakes_perfect + cupcakes_burnt) * cost_per_cupcake
    net_profit = revenue - cost
    result = net_profit
    return result

print(solution())
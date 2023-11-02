def solution():
    """Prudence was starting a cupcake business.  She figured that each cupcake cost $0.75 to make.  The first 2 dozen that she made burnt and she had to throw them out.  The next 2 came out perfectly and she ended up eating 5 cupcakes right away.  Later that day she made 2 more dozen cupcakes and decided to eat 4 more. If she sells the remaining cupcakes at $2.00 each, how much is her net profit?"""
    cost_per_cupcake = 0.75
    burnt_cupcakes = 2 * 12
    perfect_cupcakes = 2 * 12
    eaten_cupcakes = 5 + 4
    remaining_cupcakes = (burnt_cupcakes + perfect_cupcakes) - eaten_cupcakes
    revenue = remaining_cupcakes * 2
    total_cost = (burnt_cupcakes + perfect_cupcakes + remaining_cupcakes) * cost_per_cupcake
    net_profit = revenue - total_cost
    result = net_profit
    return result

print(solution())
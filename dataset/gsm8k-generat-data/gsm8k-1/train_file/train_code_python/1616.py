def solution():
    """Joe sells ham and cheese sandwiches for $1.50. If a slice of bread costs $0.15, a slice of ham costs $0.25 and a slice of cheese costs $0.35, how many cents does a sandwich with one slice of each protein cost Joe to make?"""
    bread_cost = 0.15
    ham_cost = 0.25
    cheese_cost = 0.35
    cost_per_sandwich = bread_cost + ham_cost + cheese_cost
    cost_in_cents = cost_per_sandwich * 100
    result = cost_in_cents
    return result

print(solution())
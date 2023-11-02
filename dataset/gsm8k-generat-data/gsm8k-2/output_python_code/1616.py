def solution():
    """Joe sells ham and cheese sandwiches for $1.50. If a slice of bread costs $0.15, a slice of ham costs $0.25 and a slice of cheese costs $0.35, how many cents does a sandwich with one slice of each protein cost Joe to make?"""
    bread_cost = 0.15
    ham_cost = 0.25
    cheese_cost = 0.35
    sandwich_cost = bread_cost * 2 + ham_cost + cheese_cost
    result = sandwich_cost * 100
    return result

print(solution())
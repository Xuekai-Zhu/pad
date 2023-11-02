def solution():
    """Julio makes a mocktail every evening. He uses 1 tablespoon of lime juice and tops with 1 cup of sparkling water. He can usually squeeze 2 tablespoons of lime juice per lime. After 30 days, if limes are 3 for $1.00, how much will he have spent on limes?"""
    num_limes_used = 30
    tablespoons_per_lime = 2
    tablespoons_per_mocktail = 1
    total_tablespoons = num_limes_used * tablespoons_per_lime * tablespoons_per_mocktail
    num_limes_needed = (total_tablespoons / tablespoons_per_lime) + 1
    cost_per_lime = 1/3
    total_cost = num_limes_needed * cost_per_lime
    result = total_cost
    return result

print(solution())
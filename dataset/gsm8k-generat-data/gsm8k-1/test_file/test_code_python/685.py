def solution():
    """Manolo bought five lollipops and four candies that cost $3.20. If each lollipop costs $0.40, how much will 10 lollipops and 10 candies cost him?"""
    lollipop_cost = 0.4
    candies_cost = (3.20 - 5 * lollipop_cost) / 4
    total_cost = 10 * lollipop_cost + 10 * candies_cost
    result = total_cost
    return result

print(solution())
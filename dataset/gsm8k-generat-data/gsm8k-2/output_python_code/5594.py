def solution():
    """When Matty was born, the cost of a ticket to Mars was $1,000,000. The cost is halved every 10 years. How much will a ticket cost when Matty is 30?"""
    initial_cost = 1000000
    halving_time = 10
    years_passed = 30
    halving_count = years_passed // halving_time
    final_cost = initial_cost / (2**halving_count)
    result = final_cost
    return result

print(solution())
def solution():
    """James has to buy insurance. Since he had an accident it was 60% more than normal. The normal cost is $120 a month. How much does he pay a year?"""
    normal_cost = 120 * 12
    percent_increase = 60
    increased_cost = normal_cost * (1 + (percent_increase / 100))
    total_cost = increased_cost * 1
    result = total_cost
    return result

print(solution())
def solution():
    """A company spends $15000 on advertising for a year, and then spends a third of that amount on advertising for another year. What's the total amount the company spent on advertising for the two years?"""
    year1_cost = 15000
    year2_cost = year1_cost / 3
    total_cost = year1_cost + year2_cost
    result = total_cost
    return result

print(solution())
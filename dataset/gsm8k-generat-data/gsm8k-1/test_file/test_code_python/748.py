def solution():
    """Jenna has 4 roommates. Each month the electricity bill is $100. How much will each roommate pay per year for electricity, if they divide the share equally?"""
    num_roommates = 4
    cost_per_month = 100
    months_per_year = 12
    total_cost = cost_per_month * months_per_year
    cost_per_person = total_cost / num_roommates
    result = cost_per_person
    return result

print(solution())
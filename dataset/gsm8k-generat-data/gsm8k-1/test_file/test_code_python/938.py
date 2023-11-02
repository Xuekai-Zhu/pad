def solution():
    """Patty's Plumbing charges $40 to visit a house to make a repair, plus $35 per hour, or part thereof, for labor, plus parts. One job took 2.25 hours and used $60 in parts. How much did Patty charge?"""
    visit_charge = 40
    labor_charge_per_hour = 35
    labor_time = 2.25
    parts_charge = 60
    labor_cost = round(labor_time * labor_charge_per_hour)
    total_cost = visit_charge + labor_cost + parts_charge
    result = total_cost
    return result

print(solution())
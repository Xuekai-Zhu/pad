def solution():
    """Toby is filling his swimming pool for the summer. The pool normally takes 50 hours to fill. He knows his hose runs at 100 gallons per hour. Water costs 1 cent for 10 gallons. How many dollars does it cost to fill the pool?"""
    pool_fill_time = 50
    hose_rate = 100
    total_gallons = pool_fill_time * hose_rate
    cost_per_gallon = 0.1
    total_cost = (total_gallons * cost_per_gallon) / 100
    result = total_cost
    return result

print(solution())
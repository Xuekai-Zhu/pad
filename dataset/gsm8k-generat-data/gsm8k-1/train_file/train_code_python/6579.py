def solution():
    """Toby is filling his swimming pool for the summer. The pool normally takes 50 hours to fill. He knows his hose runs at 100 gallons per hour. Water costs 1 cent for 10 gallons. How many dollars does it cost to fill the pool?"""
    hours_to_fill = 50
    gallons_per_hour = 100
    total_gallons = hours_to_fill * gallons_per_hour
    cost_per_gallon = 0.1
    total_cost = total_gallons * cost_per_gallon
    result = total_cost
    return result

print(solution())
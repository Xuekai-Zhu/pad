def solution():
    """Mark was caught speeding and the judge wants to make an example out of him. The base fine for speeding is $50 but additional penalties apply in this case. The fine is increased by $2 for every mile per hour Mark was going over the speed limit. He was going 75 miles per hour in a 30 mile per hour zone. The fine is also doubled because he was in a school zone. Finally, the judge makes Mark pay $300 in court costs and he also has to pay his lawyer $80/hour for three hours of work. How much does Mark owe for this speeding ticket?"""
    base_fine = 50
    speed_limit = 30
    mark_speed = 75
    over_speed = mark_speed - speed_limit
    fine = base_fine + (2 * over_speed)
    fine *= 2
    court_costs = 300
    lawyer_fee = 80 * 3
    total_cost = fine + court_costs + lawyer_fee
    result = total_cost
    return result

print(solution())
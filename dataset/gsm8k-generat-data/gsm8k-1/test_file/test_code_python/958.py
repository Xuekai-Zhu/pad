def solution():
    """Jen decides to travel to 3 different countries. He has to pay $400 for the supplies he needs, in total. The tickets for travel cost, in total, 50% more than the supplies. How much does travel cost?"""
    supply_cost = 400
    ticket_cost_increase = 0.5
    ticket_cost = supply_cost * ticket_cost_increase
    total_cost = supply_cost + ticket_cost
    result = total_cost
    return result

print(solution())
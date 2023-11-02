def solution():
    
    total_budget = 40
    num_people = 2
    ticket_price = 5
    bus_price = 1.5 * 2 * 2  
    total_cost = ticket_price * num_people + bus_price
    remaining_budget = total_budget - total_cost
    result = remaining_budget
    return result

print(solution())
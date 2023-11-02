def solution():
    total_budget = 20
    samuel_ticket_cost = 14
    samuel_food_drinks_cost = 6
    kevin_ticket_cost = total_budget - samuel_ticket_cost
    kevin_food_drinks_cost = total_budget - (kevin_ticket_cost + 2)
    kevin_cost_total = kevin_ticket_cost + kevin_food_drinks_cost
    kevin_food_cost = kevin_cost_total - kevin_ticket_cost
    result = kevin_food_cost
    return result

print(solution())
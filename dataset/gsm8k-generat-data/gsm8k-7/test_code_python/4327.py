def solution():
    total_budget = 20
    samuel_ticket_price = 14
    samuel_food_drinks = 6
    kevin_ticket_price = total_budget - samuel_ticket_price - samuel_food_drinks - 2
    kevin_food = total_budget - samuel_ticket_price - samuel_food_drinks - kevin_ticket_price
    result = kevin_food
    return result

print(solution())
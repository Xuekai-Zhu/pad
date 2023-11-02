def solution():
     samuel_total_spent = 20
     kevin_total_spent = 20
     samuel_ticket_cost = 14
     samuel_drinks_and_food = 6
     kevin_ticket_cost = 6
     kevin_drinks = 2
     kevin_food = samuel_total_spent - samuel_ticket_cost - samuel_drinks_and_food - kevin_ticket_cost - kevin_drinks
     result = kevin_food
     return result

print(solution())
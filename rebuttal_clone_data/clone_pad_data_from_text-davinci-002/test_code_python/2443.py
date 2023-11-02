def solution():
     adult_tickets = 3
     child_tickets = 3
     adult_ticket_cost = 2
     child_ticket_cost = 1
     total_ticket_cost = (adult_tickets * adult_ticket_cost) + (child_tickets * child_ticket_cost)
     money_paid = 20
     change_received = money_paid - total_ticket_cost
     result = change_received
     return result

print(solution())
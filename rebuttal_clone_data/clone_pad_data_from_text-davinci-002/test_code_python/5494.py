def solution():
     adult_ticket = 8
     child_ticket = 3
     total_money = 35
     total_tickets = total_money // (adult_ticket + child_ticket)
     result = total_tickets
     return result

print(solution())
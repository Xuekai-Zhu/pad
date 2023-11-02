def solution():
     total_tickets = 100
     Jude_tickets = 16
     Andrea_tickets = Jude_tickets * 2
     Sandra_tickets = Jude_tickets / 2 + 4
     tickets_sold = Jude_tickets + Andrea_tickets + Sandra_tickets
     tickets_not_sold = total_tickets - tickets_sold
     result = tickets_not_sold
     return result

print(solution())
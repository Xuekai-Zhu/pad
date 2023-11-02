def solution():
     
     ticket_1 = 1
     ticket_2 = ticket_1 + 1
     ticket_3 = ticket_2 + 1
     ticket_4 = ticket_3 + 1
     ticket_5 = ticket_4 + 1
     lilys_profit = 4
     total_cost = ticket_1 + ticket_2 + ticket_3 + ticket_4 + ticket_5
     lottery_prize = total_cost - lilys_profit
     result = lottery_prize
 
     return result

print(solution())
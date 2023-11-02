def solution():
     """Lily has 5 lottery tickets to sell. She sells the first ticket for $1. She then sells each successive ticket for a dollar more than the previous ticket. She plans to keep a $4 profit and give the remaining money as the prize. How much money will the winner of the lottery receive?"""
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
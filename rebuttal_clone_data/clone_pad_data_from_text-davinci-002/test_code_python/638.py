def solution():
     cost_of_tickets = 200 * 2
     winning_tickets = 200 * 0.2
     five_dollar_winners = winning_tickets * 0.8
     ticket_prizes = (five_dollar_winners * 5) + (winning_tickets * 10) + 5000
     profit = ticket_prizes - cost_of_tickets
     result = profit
     return result

print(solution())
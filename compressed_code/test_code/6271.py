def solution():
    
    num_tickets = 200
    ticket_cost = 2
    win_percent = 0.2
    num_winners = int(num_tickets * win_percent)
    num_big_winners = 1
    num_small_winners = int(num_winners * 0.8) 
    big_winner_payoff = 5000
    small_winner_payoff = 5
    average_small_winner_payoff = 10
    
    total_cost = num_tickets * ticket_cost
    total_winnings = (num_big_winners * big_winner_payoff) + \
                    (num_small_winners * small_winner_payoff) + \
                    ((num_winners - num_small_winners - num_big_winners) * average_small_winner_payoff)
    profit = total_winnings - total_cost
    result = profit
    return result

print(solution())
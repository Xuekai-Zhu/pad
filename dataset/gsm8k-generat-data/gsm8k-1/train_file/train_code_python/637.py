def solution():
    """James buys 200 lotto tickets for 2 dollars each. Of those tickets 20% are winners. 80% of the winners are for 5 dollars. 1 ticket is the grand prize of $5,000. The other tickets win an average of $10. How much did he profit?"""
    num_tickets = 200
    ticket_cost = 2
    win_percent = 0.2
    num_winners = int(num_tickets * win_percent)
    num_big_winners = 1
    num_small_winners = int(num_winners * 0.8) # 80% are small winners
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
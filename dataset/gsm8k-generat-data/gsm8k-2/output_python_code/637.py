def solution():
    """James buys 200 lotto tickets for 2 dollars each. Of those tickets 20% are winners.
    80% of the winners are for 5 dollars. 1 ticket is the grand prize of $5,000.
    The other tickets win an average of $10. How much did he profit?"""
    num_tickets = 200
    ticket_cost = 2
    win_percentage = 0.2
    num_winners = int(num_tickets * win_percentage)
    num_big_winners = 1
    num_small_winners = int(num_winners * 0.8)
    num_average_winners = num_winners - num_big_winners - num_small_winners
    big_win_amount = 5000
    small_win_amount = 5
    average_win_amount = 10

    total_cost = num_tickets * ticket_cost
    total_winnings = (num_big_winners * big_win_amount) + \
                     (num_small_winners * small_win_amount) + \
                     (num_average_winners * average_win_amount)

    profit = total_winnings - total_cost
    result = profit
    return result

print(solution())
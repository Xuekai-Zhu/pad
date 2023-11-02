def solution():
    """James buys 200 lotto tickets for 2 dollars each. Of those tickets 20% are winners. 80% of the winners are for 5 dollars. 1 ticket is the grand prize of $5,000. The other tickets win an average of $10. How much did he profit?"""
    # Define the information given in the problem
    num_tickets = 200
    ticket_cost = 2
    win_percent = 0.2
    win_small_percent = 0.8
    win_small_amount = 5
    grand_prize = 5000
    win_average = 10

    # Calculate the total cost of the tickets
    total_cost = num_tickets * ticket_cost

    # Calculate the number of winning tickets
    num_winning_tickets = int(num_tickets * win_percent)

    # Calculate the number of small winning tickets
    num_small_tickets = int(num_winning_tickets * win_small_percent)

    # Calculate the total amount won with the small winning tickets
    small_winnings = num_small_tickets * win_small_amount

    # Calculate the total amount won with the grand prize ticket and the average winning tickets
    grand_winnings = grand_prize + (num_winning_tickets - num_small_tickets) * win_average

    # Calculate the total profit
    total_profit = grand_winnings - total_cost + small_winnings

    result = total_profit
    return result

print(solution())
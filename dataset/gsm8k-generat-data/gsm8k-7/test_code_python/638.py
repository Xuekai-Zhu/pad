def solution():
    num_tickets = 200
    ticket_cost = 2.0
    win_percentage = 0.2
    win_5dollar_percentage = 0.8
    grand_prize = 5000
    average_win = 10

    # Calculate the total cost of all tickets
    total_cost = num_tickets * ticket_cost

    # Calculate the total number of winning tickets
    total_winners = int(num_tickets * win_percentage)

    # Calculate the number of winning tickets that are worth $5
    winners_5_dollars = int(total_winners * win_5dollar_percentage)

    # Calculate the total winnings from the $5 prizes
    total_winnings_5_dollars = winners_5_dollars * 5

    # Calculate the total winnings from the grand prize
    total_grand_prize = grand_prize

    # Calculate the total winnings from the average win
    total_average_win = (total_winners - winners_5_dollars) * average_win

    # Calculate the total profit
    total_profit = (total_winnings_5_dollars + total_grand_prize + total_average_win) - total_cost
    result = total_profit
    return result

print(solution())
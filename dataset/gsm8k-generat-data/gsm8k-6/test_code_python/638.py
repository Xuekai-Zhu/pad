def solution():
    # Calculate the cost of buying 200 lotto tickets
    ticket_cost = 200 * 2

    # Calculate the number of winning tickets
    winning_tickets = 0.2 * 200
    
    # Calculate the winnings from the winning tickets
    winnings = (0.8 * winning_tickets * 5) + (1 * 5000) + (0.2 * winning_tickets * 10)

    # Calculate the profit
    profit = winnings - ticket_cost
    result = profit
    return result

print(solution())
def solution():
    num_tickets = 5
    first_ticket_price = 1
    profit = 4

    # Calculate the total cost of all tickets
    total_ticket_cost = sum(range(first_ticket_price, first_ticket_price + num_tickets))

    # Subtract the profit from the total cost of all tickets
    total_prize_money = total_ticket_cost - profit
    result = total_prize_money/num_tickets
    return result

print(solution())
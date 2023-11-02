def solution():
    # Cost of the first 2 tickets
    ticket_1 = 150
    ticket_2 = 150
    total_cost = ticket_1 + ticket_2

    # Cost of the third ticket
    ticket_3 = ticket_1 / 3
    total_cost += ticket_3

    # Roommate pays half the cost
    total_cost *= 0.5

    # Calculate the amount of money left in the bank
    remaining_money = 500 - total_cost
    result = remaining_money
    return result

print(solution())
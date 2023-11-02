def solution():
    num_tickets = 4
    ticket_price = 90
    current_money = 189

    # Calculate the total cost of all tickets
    total_cost = num_tickets * ticket_price

    # Calculate the amount of money Daria needs to earn
    additional_money = total_cost - current_money
    result = additional_money
    return result

print(solution())
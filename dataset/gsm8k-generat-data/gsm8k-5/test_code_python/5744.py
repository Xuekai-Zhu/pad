def solution():
    olivia_money = 112  # Olivia has $112
    nigel_money = 139  # Nigel has $139
    total_money = olivia_money + nigel_money  # Total money they have
    num_of_tickets = 6  # They want to buy 6 tickets
    ticket_price = 28  # The price of one ticket is $28
    total_cost = num_of_tickets * ticket_price  # Total cost of the tickets

    # Calculate the remaining money they have
    remaining_money = total_money - total_cost
    result = remaining_money
    return result

print(solution())
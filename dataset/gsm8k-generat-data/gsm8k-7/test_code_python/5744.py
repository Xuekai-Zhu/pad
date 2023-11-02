def solution():
    olivia_money = 112
    nigel_money = 139
    num_tickets = 6
    ticket_price = 28

    # Calculate the total cost of the tickets
    total_cost = num_tickets * ticket_price

    # Calculate the total amount of money Olivia and Nigel have before buying tickets
    total_money = olivia_money + nigel_money

    # Calculate the amount of money they have left after buying tickets
    money_left = total_money - total_cost
    result = money_left
    return result

print(solution())
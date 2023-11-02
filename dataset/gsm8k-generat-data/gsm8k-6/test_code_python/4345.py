def solution():
    # Calculate the amount spent on tickets for the family
    adult_tickets_price = 9 * 2  # 2 adults with regular tickets at $9 each
    child_ticket_price = 7  # children's tickets are $2 less than the regular ticket price
    total_tickets_price = adult_tickets_price + x * child_ticket_price  # x number of children

    # Calculate the amount paid by the family
    amount_paid = 20 * 2 + 1  # two $20 bills and $1 change

    # Calculate the number of children in the family
    x = (amount_paid - total_tickets_price) / 2
    result = x
    return result

print(solution())
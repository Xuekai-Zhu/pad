def solution():
    ticket_price = 40  # price of one ticket
    num_tickets = 12  # number of tickets bought by Mr. Benson
    cost_before_discount = ticket_price * num_tickets  # cost before discount is applied

    if num_tickets > 10:
        extra_tickets = num_tickets - 10  # number of tickets that exceed 10
        discount_rate = 0.05 * extra_tickets  # calculate discount rate
        discount_amount = cost_before_discount * discount_rate  # calculate discount amount
        cost_after_discount = cost_before_discount - discount_amount  # calculate cost after discount
    else:
        cost_after_discount = cost_before_discount  # no discount applied

    result = cost_after_discount
    return result

print(solution())
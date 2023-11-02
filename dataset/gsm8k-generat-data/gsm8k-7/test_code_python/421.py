def solution():
    num_VIP_tickets = 2
    VIP_ticket_price = 100

    num_regular_tickets = 3
    regular_ticket_price = 50

    total_ticket_cost = (num_VIP_tickets * VIP_ticket_price) + (num_regular_tickets * regular_ticket_price)

    savings_after_buying_tickets = 500 - total_ticket_cost

    result = savings_after_buying_tickets
    return result

print(solution())
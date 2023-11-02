def solution():
    # Calculate the cost of the first two tickets
    first_two_tickets_cost = 150 * 2

    # Calculate the cost of the third ticket
    third_ticket_cost = first_two_tickets_cost / 3

    # Calculate the total cost of the tickets
    total_cost = first_two_tickets_cost + third_ticket_cost

    # Calculate the amount James' roommate pays
    roommate_payment = total_cost / 2

    # Calculate the amount James has left in the bank
    money_left = 500 - roommate_payment

    return money_left

print(solution())
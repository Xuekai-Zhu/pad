def solution():
    ticket_price = 40
    num_tickets = 12

    # Calculate the original cost of all tickets
    original_cost = ticket_price * num_tickets

    # Calculate the number of tickets that exceed 10
    num_discounted = max(num_tickets - 10, 0)

    # Calculate the total discount for the discounted tickets
    discount_percent = 0.05
    discount_amount = num_discounted * ticket_price * discount_percent

    # Calculate the final cost after the discount
    final_cost = original_cost - discount_amount
    result = final_cost
    return result

print(solution())
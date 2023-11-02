def solution():
    ticket_cost = 40  # Each concert ticket costs $40
    num_tickets = 12  # Mr. Benson bought 12 concert tickets

    if num_tickets > 10:
        discount = (num_tickets - 10) * 0.05 * ticket_cost  # Calculate the discount for the extra tickets
    else:
        discount = 0  # No discount if less than or equal to 10 tickets are bought

    total_cost = (num_tickets * ticket_cost) - discount  # Calculate the total cost after discount
    result = total_cost
    return result

print(solution())
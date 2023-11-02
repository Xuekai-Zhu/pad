def solution():
    # Calculate the total cost of tickets without discounts
    adult_ticket_cost = 4.25 + 3.25  # adult tickets cost $3.25 more than children's tickets
    total_cost = 2*adult_ticket_cost + 4*4.25  # two adult tickets and four children's tickets

    # Apply the discount if they bought more than 3 tickets
    if total_tickets > 3:
        total_cost -= 2  # $2 discount for buying more than 3 tickets

    result = total_cost
    return result

print(solution())
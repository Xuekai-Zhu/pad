def solution():
    age_discount = 0.3
    regular_ticket_cost = 10
    family_size = 5
    total_ticket_cost = 0

    # Calculate the total cost of tickets for the family
    for i in range(family_size):
        if i == 0:
            # Dorothy's ticket is at a discounted rate
            ticket_cost = regular_ticket_cost * (1 - age_discount)
        elif i == 1:
            # Dorothy's younger brother's ticket is free since he is under 18
            ticket_cost = 0
        elif i == 2 or i == 3 or i == 4:
            # Dorothy's parents and grandfather get regular-priced tickets
            ticket_cost = regular_ticket_cost
        total_ticket_cost += ticket_cost

    # Calculate how much money Dorothy will have left after the trip
    money_left = 70 - total_ticket_cost
    result = money_left
    return result

print(solution())
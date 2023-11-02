def solution():
    num_friends = 3
    ticket_price = 18
    snack_price = 5

    # Calculate the cost of tickets for Jeremie and her 3 friends
    total_ticket_cost = (num_friends + 1) * ticket_price

    # Calculate the cost of snacks for Jeremie and her 3 friends
    total_snack_cost = (num_friends + 1) * snack_price

    # Calculate the total cost of going to the amusement park and buying snacks for Jeremie and her 3 friends
    total_cost = total_ticket_cost + total_snack_cost
    result = total_cost
    return result

print(solution())
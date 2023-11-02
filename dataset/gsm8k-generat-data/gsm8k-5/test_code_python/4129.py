def solution():
    num_friends = 3  # Jeremie is going with 3 friends
    ticket_price = 18  # The price of one ticket is $18
    snack_price = 5  # The price of one set of snack is $5

    # Calculate the total cost for Jeremie and her friends
    total_cost = (num_friends + 1) * ticket_price  # Jeremie and her 3 friends = 4 people
    total_cost += (num_friends + 1) * snack_price  # Jeremie and her 3 friends = 4 people, each needs a set of snack

    result = total_cost
    return result

print(solution())
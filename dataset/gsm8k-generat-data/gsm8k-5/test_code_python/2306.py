def solution():
    children_price = 4.25  # Children's tickets cost $4.25
    adult_price = children_price + 3.25  # Adult tickets cost $3.25 more than children's tickets
    num_children_tickets = 4  # They bought 4 children's tickets
    num_adult_tickets = 2  # They bought 2 adult tickets
    total_tickets = num_children_tickets + num_adult_tickets  # Total number of tickets purchased
    discount = 2  # They received a $2 discount for buying more than 3 tickets

    # Calculate the total cost of the children's tickets
    children_cost = children_price * num_children_tickets

    # Calculate the total cost of the adult tickets
    adult_cost = adult_price * num_adult_tickets

    # Calculate the total cost before discount
    total_cost = children_cost + adult_cost

    # Apply the discount if total tickets purchased is more than 3
    if total_tickets > 3:
        total_cost -= discount

    result = total_cost
    return result

print(solution())
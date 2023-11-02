def solution():
    num_adults = 2  # Julia's mom and dad are adults
    num_children = 4  # Julia's grandma and three little sisters are children
    adult_ticket_price = 12
    child_ticket_price = 10

    # Calculate the total cost of the adult tickets
    total_adult_cost = num_adults * adult_ticket_price

    # Calculate the total cost of the child tickets
    total_child_cost = num_children * child_ticket_price

    # Calculate the total cost of all the tickets
    total_cost = total_adult_cost + total_child_cost
    result = total_cost
    return result

print(solution())
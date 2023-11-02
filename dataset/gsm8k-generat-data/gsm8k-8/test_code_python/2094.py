def solution():
    # Define the prices for adult and children tickets
    adult_ticket_price = 22
    child_ticket_price = 7

    # Define the number of adults and children in the family
    num_adults = 2
    num_children = 2

    # Calculate the total price for the family's admission
    total_price = (adult_ticket_price * num_adults) + (child_ticket_price * num_children)
    result = total_price
    return result

print(solution())
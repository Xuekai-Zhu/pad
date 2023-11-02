def solution():
    """Mary goes with her 3 children to the circus. Tickets cost $2 for adults and $1 for children. Mary pays with a $20 bill. How much change will she receive?"""
    # Define the number of adults and children attending
    num_adults = 1
    num_children = 3

    # Define the price of adult and children tickets
    adult_ticket_price = 2
    child_ticket_price = 1

    # Calculate the total cost of the tickets
    total_cost = (num_adults * adult_ticket_price) + (num_children * child_ticket_price)

    # Define the amount paid by Mary
    amount_paid = 20

    # Calculate the change Mary will receive
    change = amount_paid - total_cost

    # Return the result
    result = change
    return result

print(solution())
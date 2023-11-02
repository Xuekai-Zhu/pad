def solution():
    """A family went out to see a movie. The regular ticket costs $9 and the ticket for children is $2 less. They gave the cashier two $20 bills and they received a $1 change. How many children are there if there are 2 adults in the family?"""
    # Define the prices of adult and child tickets
    adult_ticket_price = 9
    child_ticket_price = adult_ticket_price - 2

    # Define the number of adults in the family
    num_adults = 2

    # Define the total amount of money given to the cashier
    total_money = 20 * 2 + 1

    # Calculate the total cost of all tickets
    total_cost = adult_ticket_price * num_adults
    num_children = 0
    while total_cost < total_money:
        # Calculate the cost of tickets for the current number of children
        child_cost = num_children * child_ticket_price
        
        # Calculate the total cost of all tickets
        total_cost = adult_ticket_price * num_adults + child_cost
        
        # Increment the number of children
        num_children += 1

    # return the result
    result = num_children - 1
    return result

print(solution())
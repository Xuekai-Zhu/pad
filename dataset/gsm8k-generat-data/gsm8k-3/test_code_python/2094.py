def solution():
    """A family is going to the amusement park. The adult tickets cost $22 for admission, and the tickets for children cost $7. The family consists of 2 adults and 2 children. What is the total price the family will pay for admission?"""
    # Define the cost of adult and child tickets
    ADULT_PRICE = 22
    CHILD_PRICE = 7

    # Define the number of adults and children in the family
    num_adults = 2
    num_children = 2

    # Calculate the total cost of adult tickets
    adult_cost = num_adults * ADULT_PRICE

    # Calculate the total cost of child tickets
    child_cost = num_children * CHILD_PRICE

    # Calculate the total cost of admission
    total_cost = adult_cost + child_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())
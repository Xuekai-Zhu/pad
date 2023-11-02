def solution():
    """In the city park, there are various attractions for kids and their parents. The entrance ticket to the park is $5, but for each attraction, you have to pay separately - such ticket costs $2 for kids and $4 for parents. How much would a family with 4 children, their parents, and her grandmother pay for visiting the park, and one attraction inside?"""
    # Define the prices
    PARK_PRICE = 5
    KID_ATTRACTION_PRICE = 2
    PARENT_ATTRACTION_PRICE = 4

    # Define the number of people in the family
    num_children = 4
    num_adults = 2
    num_seniors = 1

    # Calculate the total cost of tickets for the family
    total_ticket_cost = PARK_PRICE + (num_children * KID_ATTRACTION_PRICE) + (num_adults * PARENT_ATTRACTION_PRICE) + (num_seniors * PARENT_ATTRACTION_PRICE)

    # Display the total cost
    result = total_ticket_cost
    return result

print(solution())
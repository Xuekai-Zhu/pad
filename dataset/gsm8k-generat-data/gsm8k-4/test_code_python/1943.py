def solution():
    """In the city park, there are various attractions for kids and their parents. The entrance ticket to the park is $5, but for each attraction, you have to pay separately - such a ticket costs $2 for kids and $4 for parents. How much would a family with 4 children, their parents, and her grandmother pay for visiting the park, and one attraction inside?"""
    # Define the prices of the tickets and the number of people in the family
    park_ticket = 5
    child_ticket = 2
    parent_ticket = 4
    num_children = 4
    num_parents = 2
    num_grandparents = 1

    # Calculate the total cost of the tickets
    total_cost = (park_ticket * (num_children + num_parents + num_grandparents)) + (child_ticket + parent_ticket) * (num_children + num_parents)

    # return the result
    result = total_cost
    return result

print(solution())
def solution():
    """In the city park, there are various attractions for kids and their parents. The entrance ticket to the park is $5, but for each attraction, you have to pay separately - such ticket costs $2 for kids and $4 for parents. How much would a family with 4 children, their parents, and her grandmother pay for visiting the park, and one attraction inside?"""
    entrance_ticket = 5
    kids_ticket = 2
    parents_ticket = 4
    family_size = 6
    attraction_ticket = 2 * kids_ticket + parents_ticket
    total_cost = entrance_ticket + (family_size * attraction_ticket)
    result = total_cost
    return result

print(solution())
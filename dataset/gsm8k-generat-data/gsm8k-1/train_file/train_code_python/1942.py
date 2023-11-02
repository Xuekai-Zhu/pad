def solution():
    """In the city park, there are various attractions for kids and their parents. The entrance ticket to the park is $5, but for each attraction, you have to pay separately - such tickets cost $2 for kids and $4 for parents. How much would a family with 4 children, their parents, and her grandmother pay for visiting the park and one attraction inside?"""
    num_children = 4
    num_parents = 2
    num_grandparents = 1
    ticket_price = 5
    child_attraction_price = 2
    parent_attraction_price = 4

    total_ticket_price = (num_children * child_attraction_price) + (num_parents * parent_attraction_price) + (
            num_grandparents * ticket_price)
    result = total_ticket_price
    return result

print(solution())
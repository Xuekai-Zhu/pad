def solution():
    """Ashley and her family went to the movies on Saturday. Children’s tickets cost $4.25 and adult tickets cost $3.25 more. They were given a $2 discount for buying more than 3 tickets. How much did they spend if they bought two adult tickets and four children’s tickets?"""
    children_ticket_cost = 4.25
    adult_ticket_cost = children_ticket_cost + 3.25
    num_children_tickets = 4
    num_adult_tickets = 2
    total_tickets = num_children_tickets + num_adult_tickets
    undiscounted_price = (num_children_tickets * children_ticket_cost) + (num_adult_tickets * adult_ticket_cost)
    discount_amount = 0
    if total_tickets > 3:
        discount_amount = 2
    total_price = undiscounted_price - discount_amount
    result = total_price
    return result

print(solution())
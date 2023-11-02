def solution():
    # Define the cost of an adult ticket and a child ticket
    adult_ticket_cost = 8
    child_ticket_cost = 3

    # Define the total amount of money the adult has
    total_money = 35

    # Calculate the maximum number of children the adult can take
    max_children = (total_money - adult_ticket_cost) / child_ticket_cost

    # Round down to the nearest whole number
    max_children = int(max_children)

    result = max_children
    return result

print(solution())
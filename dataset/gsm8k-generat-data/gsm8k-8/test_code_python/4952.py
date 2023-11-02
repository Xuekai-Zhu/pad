def solution():
    # Define the ratio of children to adults
    child_to_adult_ratio = 3

    # Define the ticket prices
    adult_ticket_price = 7
    child_ticket_price = 3

    # Define the total revenue and solve for the number of adults and children
    total_revenue = 6000
    total_people = 0
    for num_adults in range(1, 100):
        num_children = child_to_adult_ratio * num_adults
        revenue = (num_adults * adult_ticket_price) + (num_children * child_ticket_price)
        if revenue == total_revenue:
            total_people = num_adults + num_children
            break

    result = total_people
    return result

print(solution())
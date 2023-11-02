def solution():
    num_adults = 1  # Mary is an adult
    num_children = 3  # Mary has 3 children
    adult_ticket_price = 2  # Adult ticket costs $2
    child_ticket_price = 1  # Child ticket costs $1
    total_price = (num_adults * adult_ticket_price) + (num_children * child_ticket_price)  # Calculate the total price
    change = 20 - total_price  # Calculate the change
    result = change
    return result

print(solution())
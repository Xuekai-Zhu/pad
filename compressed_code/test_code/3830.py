def solution():
    
    total_amount = 6000
    adult_ticket_price = 7 
    child_ticket_price = 3
    children_per_adult = 3
    total_people = 0

    for adults in range(1, 1001): 
        children = adults * children_per_adult
        if (adults * adult_ticket_price) + (children * child_ticket_price) == total_amount:
            total_people = adults + children
            break

    result = total_people
    return result

print(solution())
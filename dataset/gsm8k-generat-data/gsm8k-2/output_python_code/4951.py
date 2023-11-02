def solution():
    """Three times as many children as adults attend a concert on Saturday. An adult ticket costs $7 and a child's ticket costs $3. The theater collected a total of $6,000. How many people bought tickets?"""
    total_amount = 6000
    adult_ticket_price = 7 
    child_ticket_price = 3
    children_per_adult = 3
    total_people = 0

    for adults in range(1, 1001): #assuming max adults can be 1000
        children = adults * children_per_adult
        if (adults * adult_ticket_price) + (children * child_ticket_price) == total_amount:
            total_people = adults + children
            break

    result = total_people
    return result

print(solution())
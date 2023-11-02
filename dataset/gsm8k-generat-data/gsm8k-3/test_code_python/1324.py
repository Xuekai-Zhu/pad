def solution():
    """After working out for 3 hours, three friends go out for lunch. Adam spends two-thirds as much money on lunch as Rick. Rick and Jose eat lunch of the same price. If Jose ate lunch worth $45, what is the cost of lunch for all three?"""
    # Define the cost of lunch for Jose
    jose_cost = 45

    # Calculate the cost of lunch for Rick
    rick_cost = jose_cost * 3 / 2

    # Calculate the total cost of lunch for all three friends
    total_cost = jose_cost + rick_cost + rick_cost * 2

    # Display the total cost of lunch
    result = total_cost
    return result

print(solution())
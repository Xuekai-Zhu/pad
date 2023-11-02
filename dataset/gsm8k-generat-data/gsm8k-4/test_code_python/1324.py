def solution():
    """After working out for 3 hours, three friends go out for lunch. Adam spends two-thirds as much money on lunch as Rick. Rick and Jose eat lunch of the same price. If Jose ate lunch worth $45, what is the cost of lunch for all three?"""
    # Define the cost of Jose's lunch
    jose_lunch_cost = 45

    # Calculate Rick's lunch cost
    rick_lunch_cost = jose_lunch_cost

    # Calculate Adam's lunch cost
    adam_lunch_cost = (2/3) * rick_lunch_cost

    # Calculate the total cost of lunch for all three
    total_lunch_cost = jose_lunch_cost + rick_lunch_cost + adam_lunch_cost

    result = total_lunch_cost
    return result

print(solution())
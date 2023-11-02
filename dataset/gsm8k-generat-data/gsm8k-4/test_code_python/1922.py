def solution():
    """Stormi is saving up to buy a bicycle. She washes 3 cars for $10 each. She mows 2 lawns for $13 each. If the bicycle she wants costs $80, how much more money does Stormi need to make to afford the bicycle?"""
    # Define the income from washing cars and mowing lawns
    car_income = 3 * 10
    lawn_income = 2 * 13

    # Calculate the total income
    total_income = car_income + lawn_income

    # Define the cost of the bicycle
    bicycle_cost = 80

    # Calculate the remaining amount Stormi needs to make to afford the bicycle
    remaining_cost = bicycle_cost - total_income

    result = remaining_cost
    return result

print(solution())
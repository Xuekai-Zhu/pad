def solution():
    """Sally is saving up for a trip to Sea World. She already has $28 saved. It costs her $10 to park, $55 to get into the park and $25 for a meal pass. Sea World is 165 miles away and her car gets 30 miles per gallon of gas. If gas costs $3 a gallon, how much more will she have to save up?"""
    
    # Define the costs
    PARKING_COST = 10
    ENTRANCE_COST = 55
    MEAL_COST = 25

    # Calculate the total cost of the trip
    total_cost = PARKING_COST + ENTRANCE_COST + MEAL_COST

    # Calculate the cost of gas
    gas_cost = (165 / 30) * 3

    # Add the cost of gas to the total cost
    total_cost += gas_cost

    # Calculate the amount Sally still needs to save
    amount_left = total_cost - 28

    # Display the amount Sally still needs to save
    result = amount_left
    return result

print(solution())
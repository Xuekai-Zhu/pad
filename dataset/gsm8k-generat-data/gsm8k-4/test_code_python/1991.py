def solution():
    """Sally is saving up for a trip to Sea World. She already has $28 saved. It costs her $10 to park, $55 to get into the park and $25 for a meal pass. Sea World is 165 miles away and her car gets 30 miles per gallon of gas. If gas costs $3 a gallon, how much more will she have to save up?"""
    # Define the costs of parking, tickets, and meal pass
    PARKING_COST = 10
    TICKET_COST = 55
    MEALPASS_COST = 25

    # Define the distance to Sea World and the gas mileage of Sally's car
    DISTANCE = 165
    GAS_MILEAGE = 30

    # Define the cost per gallon of gas
    GAS_COST_PER_GALLON = 3

    # Calculate the total cost of gas for the round trip
    gas_cost = (DISTANCE / GAS_MILEAGE) * GAS_COST_PER_GALLON * 2

    # Calculate the total cost of the trip
    total_cost = PARKING_COST + TICKET_COST + MEALPASS_COST + gas_cost

    # Calculate how much more Sally needs to save up
    remaining_cost = total_cost - 28

    # Return the result
    result = remaining_cost
    return result

print(solution())
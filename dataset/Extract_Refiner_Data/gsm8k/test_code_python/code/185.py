def solution():
    
    # Define the cost of tickets and food
    TICKET_COST = 20.25
    FOOD_COST = TICKET_COST - 4.5

    # Define the cost of rides
    RIDE_COST = 33

    # Calculate the total cost of tickets and food
    total_cost = TICKET_COST + FOOD_COST + RIDE_COST

    # Calculate the cost per person
    cost_per_person = total_cost / 3

    # Display the cost per person
    result = cost_per_person
    return result

print(solution())
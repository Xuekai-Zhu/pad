def solution():
    
    # Define the hourly rates for each person
    CARLOS_RATE = 30
    BENZI_RATE = 18

    # Define the number of hours each person uses the boat and raft
    CARLOS_HOURS = 3
    BENZI_HOURS = 5

    # Calculate the total cost for each person's rental
    carlos_cost = CARLOS_RATE * CARLOS_HOURS
    benji_cost = BENZI_RATE * BENZI_HOURS

    # Calculate the total cost for both people
    total_cost = carlos_cost + benji_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())
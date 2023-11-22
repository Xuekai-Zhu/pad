def solution():
    
    # Define the capacity of each bus
    BUS_CAPACITY = 60
    MINILIS_CAPACITY = 30
    MINIVANS_CAPACITY = 15

    # Define the number of buses rented
    buses_rented = 4

    # Calculate the total capacity of the buses
    total_capacity = buses_rented * BUS_CAPACITY

    # Calculate the number of employees that can be joined
    employees_joined = (6 * MINILIS_CAPACITY) + (10 * MINIVANS_CAPACITY)

    # Display the number of employees that can be joined
    result = employees_joined
    return result

print(solution())
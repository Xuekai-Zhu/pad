def solution():
    
    # Define the number of people carried by each car
    CAR_CAPACITY = 3

    # Define the number of people carried by each bus
    BUS_CAPACITY = 35

    # Define the number of cars and buses
    num_cars = 20
    num_buses = 12

    # Calculate the total number of people carried
    total_people = (num_cars * CAR_CAPACITY) + (num_buses * BUS_CAPACITY)

    # Display the total number of people
    result = total_people
    return result

print(solution())
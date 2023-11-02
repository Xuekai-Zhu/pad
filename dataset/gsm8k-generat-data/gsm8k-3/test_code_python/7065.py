def solution():
    """For homework, Juan's teacher asked everyone in the class, to write down the different types of transportation (cars, trucks, bicycles, skateboards etc) they saw on their way home that afternoon.  After school, Juan walked home and saw the following: 15 cars, 3 bicycles, 8 pickup trucks and 1 tricycle.  How many tires in total were there on the vehicles Juan saw?"""
    # Define the number of tires on each type of vehicle
    CAR_TIRES = 4
    TRUCK_TIRES = 4
    BICYCLE_TIRES = 2
    TRICYCLE_TIRES = 3

    # Define the number of each type of vehicle Juan saw
    cars = 15
    trucks = 8
    bicycles = 3
    tricycles = 1

    # Calculate the total number of tires
    total_tires = (cars * CAR_TIRES) + (trucks * TRUCK_TIRES) + (bicycles * BICYCLE_TIRES) + (tricycles * TRICYCLE_TIRES)

    # Display the total number of tires
    result = total_tires
    return result

print(solution())
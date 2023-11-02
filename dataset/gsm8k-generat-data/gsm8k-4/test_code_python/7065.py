def solution():
    """For homework, Juan's teacher asked everyone in the class to write down the different types of transportation (cars, trucks, bicycles, skateboards, etc.) they saw on their way home that afternoon. After school, Juan walked home and saw the following: 15 cars, 3 bicycles, 8 pickup trucks, and 1 tricycle. How many tires in total were there on the vehicles Juan saw?"""
    # Define the number of tires for each type of vehicle
    cars_tires = 4
    trucks_tires = 4
    bicycles_tires = 2
    tricycle_tires = 3

    # Calculate the total number of tires
    total_tires = (15 * cars_tires) + (8 * trucks_tires) + (3 * bicycles_tires) + (1 * tricycle_tires)

    # Return the answer
    result = total_tires
    return result

print(solution())
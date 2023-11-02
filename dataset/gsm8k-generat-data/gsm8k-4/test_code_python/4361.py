def solution():
    """The tripodasaurus has three legs. In a flock of tripodasauruses, there is a total of 20 heads and legs. How many tripodasauruses are in the flock?"""
    # Define the number of legs per tripodasaurus and the total number of legs
    LEGS_PER_TRIP = 3
    total_legs = 20

    # Calculate the number of tripodasauruses in the flock using the given information
    num_trip = (total_legs / LEGS_PER_TRIP) - (total_legs / (2 * LEGS_PER_TRIP))

    # Return the solution
    result = num_trip
    return result

print(solution())
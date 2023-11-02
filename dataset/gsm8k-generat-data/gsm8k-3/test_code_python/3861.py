def solution():
    """In a town, there are four primary schools. Two of them can teach 400 students at a time, and the other two 340 students at a time. How many students at a time in total, can these four primary schools teach?"""
    # Define the capacities of the primary schools
    CAPACITY_1 = 400
    CAPACITY_2 = 340

    # Calculate the total capacity of the first two schools
    total_capacity_1 = 2 * CAPACITY_1

    # Calculate the total capacity of the second two schools
    total_capacity_2 = 2 * CAPACITY_2

    # Calculate the total capacity of all four schools
    total_capacity = total_capacity_1 + total_capacity_2

    # Display the total capacity
    result = total_capacity
    return result

print(solution())
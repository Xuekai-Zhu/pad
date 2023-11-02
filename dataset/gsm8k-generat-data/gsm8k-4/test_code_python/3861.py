def solution():
    """In a town, there are four primary schools. Two of them can teach 400 students at a time, and the other two 340 students at a time. How many students at a time in total, can these four primary schools teach?"""
    # Define the capacities of the four schools
    capacity_1 = 400
    capacity_2 = 400
    capacity_3 = 340
    capacity_4 = 340

    # Calculate the total capacity of the four schools
    total_capacity = capacity_1 + capacity_2 + capacity_3 + capacity_4

    # return the result
    result = total_capacity
    return result

print(solution())
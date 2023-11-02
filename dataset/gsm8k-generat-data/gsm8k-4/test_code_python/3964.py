def solution():
    """A conference center has six rooms. Each room can hold up to 80 people. Today, the conference center is only 2/3 full. How many people are in the conference center?"""
    # Define the number of rooms and the capacity per room
    rooms = 6
    capacity = 80

    # Calculate the total capacity of the conference center
    total_capacity = rooms * capacity

    # Calculate the number of people currently in the conference center
    current_capacity = total_capacity * (2/3)

    # Return the result
    result = current_capacity
    return result

print(solution())
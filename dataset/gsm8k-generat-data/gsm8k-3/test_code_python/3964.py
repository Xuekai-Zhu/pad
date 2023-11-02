def solution():
    """A conference center has six rooms. Each room can hold up to 80 people. Today, the conference center is only 2/3 full. How many people are in the conference center?"""
    # Define the capacity of each room
    ROOM_CAPACITY = 80

    # Define the number of rooms in the conference center
    num_rooms = 6

    # Calculate the total capacity of the conference center
    total_capacity = ROOM_CAPACITY * num_rooms

    # Calculate the number of people in the conference center, given that it is only 2/3 full
    people_in_center = total_capacity * (2/3)

    # Display the number of people in the conference center
    result = people_in_center
    return result

print(solution())
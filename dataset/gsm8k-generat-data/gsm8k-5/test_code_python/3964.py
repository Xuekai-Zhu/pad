def solution():
    max_capacity = 80  # Each room can hold up to 80 people
    num_rooms = 6  # There are six rooms in the conference center
    occupancy_rate = 2/3  # The conference center is only 2/3 full

    # Calculate the total number of people that can be accommodated
    total_capacity = max_capacity * num_rooms

    # Calculate the number of people in the conference center based on the occupancy rate
    num_people = total_capacity * occupancy_rate
    result = num_people
    return result

print(solution())
def solution():
    # Calculate the number of rooms needed to fit all the students
    # Each room can fit up to 4 students (2 on each bed) and 1 on the pull-out couch
    num_rooms = (30 // 4) + (30 % 4 > 0)  # round up to the nearest whole number
    result = num_rooms
    return result

print(solution())
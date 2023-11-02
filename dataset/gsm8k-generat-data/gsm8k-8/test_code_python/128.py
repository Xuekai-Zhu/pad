def solution():
    # Define the number of students and the maximum capacity of each room
    num_students = 30
    capacity_per_room = 2*2 + 1

    # Calculate the total number of rooms needed by dividing the number of students by the capacity per room
    total_rooms = num_students // capacity_per_room
    if num_students % capacity_per_room != 0:
        total_rooms += 1

    result = total_rooms
    return result

print(solution())
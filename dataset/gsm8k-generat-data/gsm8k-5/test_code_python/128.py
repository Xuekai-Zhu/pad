def solution():
    num_students = 30
    num_beds_per_room = 4  # 2 queen size beds = 4 beds total

    # Calculate the number of rooms needed based on the number of students and beds per room
    rooms_needed = (num_students // num_beds_per_room) + (num_students % num_beds_per_room > 0)
    result = rooms_needed
    return result

print(solution())
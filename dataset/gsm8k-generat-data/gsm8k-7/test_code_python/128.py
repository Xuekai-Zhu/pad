def solution():
    num_students = 30
    num_beds_per_room = 2
    num_students_per_pullout_couch = 1
    total_beds_needed = num_students * num_beds_per_room
    num_pullout_couches_needed = total_beds_needed - num_students
    num_rooms_needed = num_beds_per_room * (num_students // num_beds_per_room) + num_pullout_couches_needed
    result = num_rooms_needed
    return result

print(solution())
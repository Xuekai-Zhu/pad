def solution():
    """A school principal is booking hotel rooms for a class of 30 students to stay at during an overnight field trip. Each of the hotel's rooms has two queen size beds, which can fit two students each, and a pull-out couch, which can fit one student. How many rooms does the principal need to book to fit all of the students in the class?"""
    total_students = 30
    num_beds_per_room = 2
    num_students_per_bed = 2
    num_students_per_couch = 1
    num_rooms_needed = int((total_students // (num_beds_per_room * num_students_per_bed)) + ((total_students % (num_beds_per_room * num_students_per_bed)) // num_students_per_couch))
    result = num_rooms_needed
    return result

print(solution())
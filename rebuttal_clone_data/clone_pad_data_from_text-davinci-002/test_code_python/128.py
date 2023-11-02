def solution():
    """A school principal is booking hotel rooms for a class of 30 students to stay at during an overnight field trip. Each of the hotel's rooms has two queen size beds, which can fit two students each, and a pull-out couch, which can fit one student. How many rooms does the principal need to book to fit all of the students in the class?"""
    class_size = 30
    beds_per_room = 2
    couches_per_room = 1
    students_per_bed = 2
    students_per_couch = 1
    total_capacity = beds_per_room * students_per_bed + couches_per_room * students_per_couch
    number_of_rooms_needed = math.ceil(class_size / total_capacity)
    result = number_of_rooms_needed
    return result

print(solution())
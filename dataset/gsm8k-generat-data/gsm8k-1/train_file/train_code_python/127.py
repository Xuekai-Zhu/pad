def solution():
    """A school principal is booking hotel rooms for a class of 30 students to stay at during an overnight field trip. Each of the hotel's rooms has two queen size beds, which can fit two students each, and a pull-out couch, which can fit one student. How many rooms does the principal need to book to fit all of the students in the class?"""
    students = 30
    beds_per_room = 2
    capacity_per_room = beds_per_room + 1
    rooms_needed = (students // capacity_per_room) + 1 if students % capacity_per_room != 0 else students // capacity_per_room
    result = rooms_needed
    return result

print(solution())
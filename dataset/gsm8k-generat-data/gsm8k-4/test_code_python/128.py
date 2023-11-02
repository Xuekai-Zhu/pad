def solution():
    """A school principal is booking hotel rooms for a class of 30 students to stay at during an overnight field trip. Each of the hotel's rooms has two queen size beds, which can fit two students each, and a pull-out couch, which can fit one student. How many rooms does the principal need to book to fit all of the students in the class?"""
    # Define the number of students and the number of beds and couches per room
    num_students = 30
    beds_per_room = 2
    couches_per_room = 1

    # Calculate the minimum number of rooms needed to fit all the students
    num_rooms = (num_students // beds_per_room) + (num_students % beds_per_room > 0) + (num_students % beds_per_room % couches_per_room > 0)

    # return the result
    result = num_rooms
    return result

print(solution())
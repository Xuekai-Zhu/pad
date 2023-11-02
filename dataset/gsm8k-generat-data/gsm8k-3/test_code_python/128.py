def solution():
    """A school principal is booking hotel rooms for a class of 30 students to stay at during an overnight field trip. Each of the hotel's rooms has two queen size beds, which can fit two students each, and a pull-out couch, which can fit one student. How many rooms does the principal need to book to fit all of the students in the class?"""
    
    # Calculate the number of students that can sleep on the beds
    beds_capacity = 2 * 2  # each room has 2 queen size beds, which can fit 2 students each
    beds_sleeper = beds_capacity * num_rooms
    
    # Calculate the number of students that can sleep on the pull-out couches
    couch_capacity = 1
    couch_sleeper = couch_capacity * num_rooms
    
    # Calculate the total number of students that can sleep in the hotel
    total_capacity = beds_sleeper + couch_sleeper
    
    # Calculate the number of rooms needed to accommodate all students in the class
    num_rooms = math.ceil(total_capacity / num_students)
    
    result = num_rooms
    return result

print(solution())
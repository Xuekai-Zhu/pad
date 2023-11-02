def solution():
    """Carla is taking attendance for her sixth-grade class. She knows that 2 students are in the restroom, and one less than three times that number of students are absent. If there are four rows with six desks each that are all 2/3 full, how many students does Carla teach, including the ones in and out of the classroom?"""
    # Find the number of absent students
    restroom = 2
    absent = 3 * restroom - 1

    # Find the number of students present in the classroom
    desks = 4 * 6
    present = round(desks * 2/3)

    # Find the total number of students
    total_students = present + absent + restroom

    # Display the total number of students
    result = total_students
    return result

print(solution())
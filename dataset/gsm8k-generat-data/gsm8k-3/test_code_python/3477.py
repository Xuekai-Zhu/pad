def solution():
    """Mr. Johnson is organizing the school Christmas play and needs 50 volunteers to help with decorating the auditorium. 5 students from each of the school’s 6 math classes have volunteered to help. 13 teachers have also volunteered to help. How many more volunteers will Mr. Johnson need?"""
    # Define the number of volunteers from each math class and the total number of volunteers
    VOLUNTEERS_PER_MATH_CLASS = 5
    NUM_MATH_CLASSES = 6
    NUM_TEACHERS = 13
    TOTAL_VOLUNTEERS = (VOLUNTEERS_PER_MATH_CLASS * NUM_MATH_CLASSES) + NUM_TEACHERS

    # Define the number of volunteers needed and calculate the difference
    VOLUNTEERS_NEEDED = 50
    VOLUNTEERS_DIFFERENCE = VOLUNTEERS_NEEDED - TOTAL_VOLUNTEERS

    # Display the number of additional volunteers needed
    result = VOLUNTEERS_DIFFERENCE
    return result

print(solution())
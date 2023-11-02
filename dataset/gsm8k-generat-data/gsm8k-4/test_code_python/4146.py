def solution():
    """At Roosevelt high school there are 600 students in the senior class. A fifth of the students are in the marching band. Of the students in the marching band, half of them play a brass instrument. Of the students that play a brass instrument, a fifth of them play the saxophone. Of the students that play the saxophone, a third of them play the alto saxophone. How many students play the alto saxophone?"""
    # Define the total number of senior students
    total_students = 600

    # Calculate the number of students in the marching band
    marching_band_students = total_students / 5

    # Calculate the number of students who play a brass instrument
    brass_instrument_students = marching_band_students / 2

    # Calculate the number of students who play the saxophone
    saxophone_students = brass_instrument_students / 5

    # Calculate the number of students who play the alto saxophone
    alto_saxophone_students = saxophone_students / 3

    # return the result
    result = alto_saxophone_students
    return result

print(solution())
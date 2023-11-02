def solution():
    """At Roosevelt high school there are 600 students in the senior class. A fifth of the students are in the marching band. Of the students in the marching band, half of them play a brass instrument. Of the students that play a brass instrument, a fifth of them play the saxophone. Of the students that play the saxophone, a third of them play the alto saxophone. How many students play the alto saxophone?"""
    total_students = 600
    marching_band_students = total_students / 5
    brass_instrument_students = marching_band_students / 2
    saxophone_students = brass_instrument_students / 5
    alto_saxophone_students = saxophone_students / 3
    result = alto_saxophone_students
    return result

print(solution())
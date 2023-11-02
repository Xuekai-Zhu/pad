def solution():
    """At Roosevelt high school there are 600 students in the senior class. 
    A fifth of the students are in the marching band. 
    Of the students in the marching band, half of them play a brass instrument. 
    Of the students that play a brass instrument, a fifth of them play the saxophone. 
    Of the students that play the saxophone, a third of them play the alto saxophone. 
    How many students play the alto saxophone?"""
    # Define the number of senior students and the percentage in the marching band
    SENIOR_STUDENTS = 600
    MARCHING_BAND_PERCENTAGE = 0.2

    # Calculate the number of students in the marching band
    marching_band_students = int(SENIOR_STUDENTS * MARCHING_BAND_PERCENTAGE)

    # Calculate the number of students in the marching band who play a brass instrument
    brass_players = int(marching_band_students * 0.5)

    # Calculate the number of students in the marching band who play the saxophone
    sax_players = int(brass_players * 0.2)

    # Calculate the number of students who play the alto saxophone
    alto_sax_players = int(sax_players * 0.33)

    # Display the number of students who play the alto saxophone
    result = alto_sax_players
    return result

print(solution())
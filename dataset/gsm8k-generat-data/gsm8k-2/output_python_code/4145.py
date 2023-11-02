def solution():
    """At Roosevelt high school there are 600 students in the senior class. A fifth of the students are in the marching band. Of the students in the marching band, half of them play a brass instrument. Of the students that play a brass instrument, a fifth of them play the saxophone. Of the students that play the saxophone, a third of them play the alto saxophone. How many students play the alto saxophone?"""
    senior_class = 600
    marching_band = senior_class / 5
    brass_instrument = marching_band / 2
    saxophone = brass_instrument / 5
    alto_saxophone = saxophone / 3
    result = alto_saxophone
    return result

print(solution())
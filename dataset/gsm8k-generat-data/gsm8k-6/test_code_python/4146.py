def solution():
    # Calculate the number of students in the senior class who play the alto saxophone
    students_in_marching_band = 600 // 5  # a fifth of the students are in the marching band
    students_play_brass = students_in_marching_band // 2  # half of the students in the marching band play a brass instrument
    students_play_sax = students_play_brass // 5  # a fifth of the students who play brass play the saxophone
    students_play_alto_sax = students_play_sax // 3  # a third of the students who play the saxophone play the alto saxophone
    result = students_play_alto_sax
    return result

print(solution())
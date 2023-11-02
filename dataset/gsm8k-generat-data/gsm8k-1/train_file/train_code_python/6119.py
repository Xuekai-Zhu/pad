def solution():
    """Out of the 200 students in a class, thirty percent like the color blue. Among the remaining students who don't like the color blue, 40% like the color red, and the rest like the color yellow. Calculate the combined number of students who like the color yellow and the color blue."""
    total_students = 200
    blue_percent = 30
    blue_students = total_students * (blue_percent / 100)
    non_blue_students = total_students - blue_students
    red_percent = 40
    red_students = non_blue_students * (red_percent / 100)
    yellow_students = non_blue_students - red_students
    combined_students = blue_students + yellow_students
    result = combined_students
    return result

print(solution())
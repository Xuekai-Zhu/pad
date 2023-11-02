def solution():
    """Out of the 200 students in a class, thirty percent like the color blue. Among the remaining students who don't like the color blue, 40% like the color red, and the rest like the color yellow. Calculate the combined number of students who like the color yellow and the color blue."""
    total_students = 200
    blue_percentage = 0.3
    blue_students = total_students * blue_percentage
    non_blue_students = total_students - blue_students
    red_percentage = 0.4
    yellow_percentage = 1 - red_percentage
    yellow_students = non_blue_students * yellow_percentage
    combined_students = blue_students + yellow_students

    result = combined_students
    return result

print(solution())
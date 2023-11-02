def solution():
    """Out of the 200 students in a class, thirty percent like the color blue. Among the remaining students who don't like the color blue, 40% like the color red, and the rest like the color yellow. Calculate the combined number of students who like the color yellow and the color blue."""
    # Define the total number of students
    total_students = 200

    # Calculate the number of students who like the color blue
    blue_students = total_students * 0.3

    # Calculate the number of students who don't like the color blue
    nonblue_students = total_students - blue_students

    # Calculate the number of non-blue students who like the color red
    red_students = nonblue_students * 0.4

    # Calculate the number of non-blue students who like the color yellow
    yellow_students = nonblue_students - red_students

    # Calculate the total number of students who like either blue or yellow
    combined_students = blue_students + yellow_students

    # return the result
    result = combined_students
    return result

print(solution())
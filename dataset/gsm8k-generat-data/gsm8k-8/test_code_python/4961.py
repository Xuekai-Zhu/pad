def solution():
    # Calculate the number of students who wore lipstick
    lipstick_students = 200 / 2

    # Calculate the number of students who wore red lipstick
    red_lipstick_students = lipstick_students / 4

    # Calculate the number of students who wore blue lipstick
    blue_lipstick_students = red_lipstick_students / 5

    result = blue_lipstick_students
    return result

print(solution())
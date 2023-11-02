def solution():
    """On national lipstick day, half of the students who attended class wore colored lipstick.  Of those students who wore lipstick, one quarter wore red lipstick.  There were one-fifth as many students wearing blue lipstick as were wearing red lipstick.  If 200 students attended school that day, how many wore blue lipstick?"""
    # Calculate the number of students who wore colored lipstick
    colored_lipstick_students = 200 // 2

    # Calculate the number of students who wore red lipstick
    red_lipstick_students = colored_lipstick_students // 4

    # Calculate the number of students who wore blue lipstick
    blue_lipstick_students = red_lipstick_students // 5

    # Display the number of students who wore blue lipstick
    result = blue_lipstick_students
    return result

print(solution())
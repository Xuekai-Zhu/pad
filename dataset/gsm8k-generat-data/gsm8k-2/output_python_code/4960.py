def solution():
    """On national lipstick day, half of the students who attended class wore colored lipstick. Of those students who wore lipstick, one quarter wore red lipstick. There were one-fifth as many students wearing blue lipstick as were wearing red lipstick. If 200 students attended school that day, how many wore blue lipstick?"""
    total_students = 200
    colored_lipstick_students = total_students / 2
    red_lipstick_students = colored_lipstick_students / 4
    blue_lipstick_students = red_lipstick_students / 5
    result = blue_lipstick_students
    return result

print(solution())
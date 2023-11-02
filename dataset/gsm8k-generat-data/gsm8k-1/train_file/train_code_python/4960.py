def solution():
    """On national lipstick day, half of the students who attended class wore colored lipstick. Of those students who wore lipstick, one quarter wore red lipstick. There were one-fifth as many students wearing blue lipstick as were wearing red lipstick. If 200 students attended school that day, how many wore blue lipstick?"""
    total_students = 200
    colored_lipstick = total_students / 2
    red_lipstick = colored_lipstick / 4
    blue_lipstick = red_lipstick / 5
    result = blue_lipstick
    return result

print(solution())
def solution():
    """On national lipstick day, half of the students who attended class wore colored lipstick. Of those students who wore lipstick, one quarter wore red lipstick. There were one-fifth as many students wearing blue lipstick as were wearing red lipstick. If 200 students attended school that day, how many wore blue lipstick?"""
    # Define the total number of students and the proportion wearing lipstick
    total_students = 200
    lipstick_proportion = 0.5

    # Calculate the number of students wearing lipstick
    lipstick_students = total_students * lipstick_proportion

    # Calculate the number of students wearing red lipstick
    red_lipstick_students = lipstick_students * 0.25

    # Calculate the number of students wearing blue lipstick
    blue_lipstick_students = red_lipstick_students * 0.2

    result = round(blue_lipstick_students)
    return result

print(solution())
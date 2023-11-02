def solution():
    """There are three times as many girls as boys in the Biology class. The Physics class has 200 students. If the Biology class has half as many students as the Physics class, how many boys are in the Biology class?"""
    # Calculate the number of students in the Biology class
    biology_students = 200 / 2

    # Calculate the number of girls in the Biology class
    biology_girls = biology_students * 3/4

    # Calculate the number of boys in the Biology class
    biology_boys = biology_students - biology_girls

    result = biology_boys
    return result

print(solution())
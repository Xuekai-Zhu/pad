def solution():
    """There are three times as many girls as boys in the Biology class. The Physics class has 200 students. If the Biology class has half as many students as the Physics class, how many boys are in the Biology class?"""
    physics_students = 200
    biology_students = physics_students / 2
    girls_ratio = 3
    total_ratio = girls_ratio + 1
    boys_ratio = 1
    boys_in_biology = (boys_ratio / total_ratio) * biology_students
    result = boys_in_biology

    return result

print(solution())
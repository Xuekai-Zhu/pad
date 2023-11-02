def solution():
    """There are three times as many girls as boys in the Biology class. The Physics class has 200 students. If the Biology class has half as many students as the Physics class, how many boys are in the Biology class?"""
    physics_class = 200
    biology_class = physics_class / 2
    girls = 3 * biology_class / 4
    boys = biology_class / 4
    result = boys
    return result

print(solution())
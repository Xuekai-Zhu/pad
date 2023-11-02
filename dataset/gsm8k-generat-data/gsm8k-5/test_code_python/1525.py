def solution():
    physics_class = 200  # The Physics class has 200 students
    biology_class = physics_class / 2  # The Biology class has half as many students as the Physics class
    girls = 3 * biology_class / 4  # There are three times as many girls as boys, and girls make up 3/4 of the class
    boys = biology_class / 4  # Boys make up 1/4 of the class

    result = boys
    return result

print(solution())
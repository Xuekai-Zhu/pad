def solution():
    """A public official wants to donate 5 new soccer balls per each class in two schools. Each school has 4 elementary school classes and 5 middle school classes. How many soccer balls would the public official donate in all?"""
    classes_per_school = 4 + 5
    num_schools = 2
    soccer_balls_per_class = 5
    total_soccer_balls = classes_per_school * num_schools * soccer_balls_per_class
    result = total_soccer_balls
    return result

print(solution())
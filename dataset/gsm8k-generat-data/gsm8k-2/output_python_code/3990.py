def solution():
    """A public official wants to donate 5 new soccer balls per each class in two schools. Each school has 4 elementary school classes and 5 middle school classes. How many soccer balls would the public official donate in all?"""
    num_classes_per_school = 4 + 5
    num_balls_per_class = 5
    num_schools = 2
    total_num_balls = num_classes_per_school * num_balls_per_class * num_schools
    result = total_num_balls
    return result

print(solution())
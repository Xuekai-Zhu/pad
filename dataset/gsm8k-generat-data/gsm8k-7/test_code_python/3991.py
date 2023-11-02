def solution():
    num_classes_per_school = 9
    num_schools = 2
    num_balls_per_class = 5

    # Calculate the total number of classes in both schools
    total_classes = num_classes_per_school * num_schools

    # Calculate the total number of soccer balls donated
    total_balls = total_classes * num_balls_per_class
    result = total_balls
    return result

print(solution())
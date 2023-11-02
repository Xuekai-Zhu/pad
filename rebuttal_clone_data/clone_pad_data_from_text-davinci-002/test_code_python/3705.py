def solution():
    girls_average = 45
    boys_average = 55
    num_girls = 5
    num_boys = 5
    num_students = num_girls + num_boys
    total_average = (girls_average * num_girls + boys_average * num_boys) / num_students
    result = total_average
    return result

print(solution())
def solution():
    boys = 40
    girls = 60
    boy_score = 80
    girl_score = 90
    class_average = ((boys * boy_score) + (girls * girl_score)) / (boys + girls)
    result = class_average
    return result

print(solution())
def solution():
    """Out of the 150 students, 60% are girls and the rest are boys. Only 1/3 of the boys joined varsity clubs. How many of the boys did not join varsity clubs?"""
    total_students = 150
    girl_percent = 60
    boy_percent = 100 - girl_percent
    boys = (boy_percent / 100) * total_students
    varsity_boys = (1 / 3) * boys
    non_varsity_boys = boys - varsity_boys
    result = non_varsity_boys
    return result

print(solution())
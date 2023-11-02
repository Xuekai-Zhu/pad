def solution():
    """Out of the 150 students, 60% are girls and the rest are boys. Only 1/3 of the boys joined varsity clubs. How many of the boys did not join varsity clubs?"""
    total_students = 150
    percent_girls = 60
    percent_boys = 100 - percent_girls
    boys = (total_students * percent_boys) / 100
    varsity_boys = boys / 3
    non_varsity_boys = boys - varsity_boys
    result = non_varsity_boys
    
    return result

print(solution())
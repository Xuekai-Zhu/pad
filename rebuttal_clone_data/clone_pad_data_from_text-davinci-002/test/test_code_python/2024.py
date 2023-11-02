def solution():
    total_students = 800
    percent_girls = 5/8
    percent_boys = 1 - percent_girls
    girls = total_students * percent_girls
    boys = total_students * percent_boys
    percent_girls_primary = 7/10
    percent_girls_middle = 1 - percent_girls_primary
    percent_boys_primary = 2/5
    percent_boys_middle = 1 - percent_boys_primary
    girls_primary = girls * percent_girls_primary
    girls_middle = girls * percent_girls_middle
    boys_primary = boys * percent_boys_primary
    boys_middle = boys * percent_boys_middle
    total_primary = girls_primary + boys_primary
    middle_schoolers = total_students - total_primary
    result = middle_schoolers
    return result

print(solution())
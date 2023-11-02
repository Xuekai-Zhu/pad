def solution():
    num_students = 150
    percent_girls = 60
    percent_boys = 100 - percent_girls
    num_boys = (percent_boys/100) * num_students
    boys_in_varsity = num_boys / 3
    boys_not_in_varsity = num_boys - boys_in_varsity
    result = boys_not_in_varsity
    return result

print(solution())
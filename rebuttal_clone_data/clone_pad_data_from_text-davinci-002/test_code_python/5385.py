def solution():
    ratio_boys_girls = "3:4"
    num_girls = 60
    percent_teachers = 20
    num_boys = num_girls * (4/3)
    total_people = num_boys + num_girls + (num_boys * (percent_teachers/100))
    result = total_people
    return result

print(solution())
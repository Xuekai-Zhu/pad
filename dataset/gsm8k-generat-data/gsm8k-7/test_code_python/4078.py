def solution():
    num_boys = 15
    num_girls = int(num_boys * 1.2)  # 20% greater than the number of boys
    num_girls *= 2  # number of girls doubled
    total_students = num_boys + num_girls
    result = total_students
    return result

print(solution())
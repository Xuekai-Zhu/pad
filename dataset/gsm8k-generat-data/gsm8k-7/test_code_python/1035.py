def solution():
    num_boys = 600
    diff_boys_girls = 400

    # Calculate the total number of girls
    num_girls = num_boys + diff_boys_girls

    # Calculate the total number of boys and girls
    total_students = num_boys + num_girls

    # Calculate 60% of the total number of boys and girls
    percent_total = 60 / 100
    result = percent_total * total_students
    return result

print(solution())
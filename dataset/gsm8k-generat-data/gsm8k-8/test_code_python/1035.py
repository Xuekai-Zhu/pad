def solution():
    # Calculate the number of girls
    num_boys = 600
    diff = 400
    num_girls = num_boys + diff

    # Calculate the total number of boys and girls
    total_students = num_boys + num_girls

    # Calculate 60% of the total number of boys and girls
    percent = 0.6
    result = percent * total_students
    return result

print(solution())
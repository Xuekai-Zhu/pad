def solution():
    # Calculate the number of students who are reading
    girls_reading = (5/6) * 12
    boys_reading = (4/5) * 10
    total_reading = girls_reading + boys_reading

    # Calculate the number of students who are not reading
    total_students = 12 + 10
    not_reading = total_students - total_reading
    result = not_reading
    return result

print(solution())
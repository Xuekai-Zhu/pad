def solution():
    # Calculate the total number of boys in the class
    total_students = 250
    girls_present = 140
    boys_present = total_students - girls_present
    boys_absent = boys_present / 2  # the number of girls present is twice the number of boys present

    result = boys_absent
    return result

print(solution())
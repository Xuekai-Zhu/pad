def solution():
    total_students = 250
    total_girls_present = 140

    # Calculate the number of boys present
    total_boys_present = (total_students - total_girls_present) / 3

    # Calculate the total number of boys absent
    total_boys_absent = (total_students / 3) - total_boys_present

    result = total_boys_absent
    return result

print(solution())
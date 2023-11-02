def solution():
    # Calculate the number of boys in the class
    total_students = 250  # There are 250 students in the class
    girls_present = 140  # 140 girls were present
    boys_present = (total_students - girls_present) / 3  # There were 3 boys for every 1 girl
    boys_absent = total_students / 2 - boys_present  # There were twice as many girls as boys present, so there were half as many boys absent

    result = boys_absent
    return result

print(solution())
def solution():
    num_students = 10
    avg_age_9 = 8
    new_age = 28

    # Calculate the total age of 9 students
    total_age_9 = num_students * avg_age_9 - new_age

    # Calculate the new average age of all 10 students
    new_avg_age = total_age_9 / num_students
    increase = new_avg_age - avg_age_9
    result = increase
    return result

print(solution())
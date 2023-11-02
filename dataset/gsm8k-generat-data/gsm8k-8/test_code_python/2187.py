def solution():
    # Define the initial variables
    num_students = 10
    avg_age_9 = 8
    total_age_9 = avg_age_9 * 9
    tenth_student_age = 28

    # Calculate the new total age and average age
    total_age_10 = total_age_9 + tenth_student_age
    new_avg_age = total_age_10 / num_students

    # Calculate the increase in average age
    increase_in_avg_age = new_avg_age - avg_age_9
    result = increase_in_avg_age
    return result

print(solution())
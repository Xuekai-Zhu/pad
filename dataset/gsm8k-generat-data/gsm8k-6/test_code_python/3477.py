def solution():
    # Calculate the total number of volunteers
    math_students = 6 * 5  # 5 students from each of the 6 math classes
    total_volunteers = math_students + 13  # math students + teachers

    # Calculate the number of additional volunteers needed
    additional_volunteers = 50 - total_volunteers
    result = additional_volunteers
    return result

print(solution())
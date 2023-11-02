def solution():
    # Calculate the number of questions for the first group
    first_group = 6 * 2

    # Calculate the number of questions for the second group
    second_group = 11 * 2

    # Calculate the number of questions for the third group
    inquisitive_person = 3 * 2
    normal_people = 8 - 1
    third_group = inquisitive_person + normal_people * 2

    # Calculate the number of questions for the last group
    last_group = 7 * 2

    # Calculate the total number of questions
    total_questions = first_group + second_group + third_group + last_group
    result = total_questions
    return result

print(solution())
def solution():
    first_group = 6
    second_group = 11
    third_group = 8
    fourth_group = 7
    
    total_people = first_group + second_group + third_group + fourth_group
    average_questions = total_people / 4
    result = total_people * average_questions
    return result

print(solution())
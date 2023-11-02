def solution():
    total_students = 42
    kindergartners = 14
    first_graders = 24

    # Calculate the number of second graders
    second_graders = total_students - kindergartners - first_graders
    result = second_graders
    return result

print(solution())
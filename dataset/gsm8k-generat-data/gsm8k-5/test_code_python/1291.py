def solution():
    total_students = 42  # Ms. Watson has 42 students in total
    kindergartners = 14  # Ms. Watson has 14 kindergartners
    first_graders = 24  # Ms. Watson has 24 first graders
    second_graders = total_students - kindergartners - first_graders  # Calculate the number of second graders

    result = second_graders
    return result

print(solution())
def solution():
    num_students = 450

    num_oranges = 70
    num_pears = 120
    num_apples = 147

    # Calculate the total number of students who picked strawberries
    num_strawberries = num_students - num_oranges - num_pears - num_apples
    result = num_strawberries
    return result

print(solution())
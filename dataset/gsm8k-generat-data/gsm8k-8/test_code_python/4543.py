def solution():
    # Define the number of students who like oranges, pears, and apples
    oranges = 70
    pears = 120
    apples = 147

    # Calculate the total number of students who were interviewed
    total_students = 450

    # Calculate the number of students who like strawberries
    strawberries = total_students - (oranges + pears + apples)

    result = strawberries
    return result

print(solution())
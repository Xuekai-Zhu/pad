def solution():
    # Calculate the number of students who like neither food
    total_students = 25
    fries_only = 15 - 6  # number of students who like only French fries
    burgers_only = 10 - 6  # number of students who like only burgers
    neither = total_students - fries_only - burgers_only - 6  # subtracting the number who like both from total
    result = neither
    return result

print(solution())
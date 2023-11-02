def solution():
    # Calculate the total number of hands in Peter's class including his
    total_hands = 20 + 2  # Peter has 2 hands
    # Divide the total number of hands by 2 to get the total number of students in Peter's class including him
    total_students = total_hands // 2
    result = total_students
    return result

print(solution())
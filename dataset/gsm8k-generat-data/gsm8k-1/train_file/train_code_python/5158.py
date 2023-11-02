def solution():
    """There are 20 hands in Peter’s class, not including his. Assume every student in the class has 2 arms and 2 hands. How many students are in Peter’s class including him?"""
    total_hands = 20
    hands_per_student = 2
    total_students = int(total_hands / hands_per_student) + 1
    result = total_students
    return result

print(solution())
def solution():
    """There are 20 hands in Peter’s class, not including his. Assume every student in the class has 2 arms and 2 hands. How many students are in Peter’s class including him?"""
    total_hands = 20
    total_students = total_hands // 2
    total_students += 1 # adding Peter
    result = total_students
    return result

print(solution())
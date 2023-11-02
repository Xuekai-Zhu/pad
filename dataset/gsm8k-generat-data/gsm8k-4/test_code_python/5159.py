def solution():
    """There are 20 hands in Peter’s class, not including his. Assume every student in the class has 2 arms and 2 hands. How many students are in Peter’s class including him?"""
    # Calculate the total number of hands in the class
    total_hands = 20 + 2  # Adding Peter's two hands

    # Calculate the total number of students in the class
    total_students = total_hands / 2

    # Add Peter as a student
    total_students += 1

    # Return the result
    result = int(total_students)
    return result

print(solution())
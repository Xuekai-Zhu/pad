def solution():
    """There are 20 hands in Peter’s class, not including his. Assume every student in the class has 2 arms and 2 hands. How many students are in Peter’s class including him?"""
    # Calculate the total number of hands in the class, including Peter's
    total_hands = 20 + 2  # Peter has 2 hands

    # Divide the total number of hands by the number of hands per student
    students = total_hands / 4

    # Display the number of students
    result = students
    return result

print(solution())
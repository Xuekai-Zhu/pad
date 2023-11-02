def solution():
    """Adam goes to a small school, which teaches 80 students in three classes. 40% of the students are in class A, and class B has 21 students fewer than class A. The rest are in class C. How many students are in this class?"""
    # Calculate the number of students in class A (40% of the total)
    classA = int(0.4 * 80)

    # Calculate the number of students in class B (21 fewer than class A)
    classB = classA - 21

    # Calculate the number of students in class C (the rest)
    classC = 80 - (classA + classB)

    # Display the number of students in class C
    result = classC
    return result

print(solution())
def solution():
    """There are 90 students who have lunch during period 5. Today, two-thirds of the students sat in the cafeteria, while the remainder sat at the covered picnic tables outside. But some yellow-jackets were attracted to their food, and so one-third of the students outside jumped up and ran inside to the cafeteria, while 3 of the students in the cafeteria went outside to see what all the fuss was about. How many students are now in the cafeteria?"""
    # Define the total number of students
    total_students = 90

    # Calculate the number of students in the cafeteria
    cafeteria_students = total_students * (2/3) - 1/3 * (total_students * (1/3)) + 3

    # Display the number of students in the cafeteria
    result = cafeteria_students
    return result

print(solution())
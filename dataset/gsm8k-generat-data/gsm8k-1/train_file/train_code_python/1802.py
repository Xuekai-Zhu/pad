def solution():
    """
    There are 90 students who have lunch during period 5. Today, two-thirds of the students sat in the cafeteria, while
    the remainder sat at the covered picnic tables outside. But some yellow-jackets were attracted to their food, and so
    one-third of the students outside jumped up and ran inside to the cafeteria, while 3 of the students in the cafeteria
    went outside to see what all the fuss was about. How many students are now in the cafeteria?
    """
    total_students = 90
    cafeteria_students = (2/3) * total_students
    picnic_students = total_students - cafeteria_students
    picnic_students_moved = (1/3) * picnic_students
    cafeteria_students_moved = 3
    new_cafeteria_students = cafeteria_students + picnic_students_moved - cafeteria_students_moved
    result = new_cafeteria_students
    return result

print(solution())
def solution():
    """There are 90 students who have lunch during period 5. Today, two-thirds of the students sat in the cafeteria, while the remainder sat at the covered picnic tables outside. But some yellow-jackets were attracted to their food, and so one-third of the students outside jumped up and ran inside to the cafeteria, while 3 of the students in the cafeteria went outside to see what all the fuss was about. How many students are now in the cafeteria?"""
    total_students = 90
    cafeteria_students = (2/3) * total_students 
    outside_students = total_students - cafeteria_students
    outside_to_cafeteria = (1/3) * outside_students
    cafeteria_to_outside = 3
    total_cafeteria = cafeteria_students + outside_to_cafeteria - cafeteria_to_outside
    result = total_cafeteria
    return result

print(solution())
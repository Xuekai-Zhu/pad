def solution():
    total_students = 90  # There are 90 students who have lunch during period 5
    cafeteria_students = total_students * (2/3)  # Two-thirds of the students sat in the cafeteria
    outside_students = total_students - cafeteria_students  # The remainder sat at the covered picnic tables outside
    outside_to_cafeteria = outside_students * (1/3)  # One-third of the students outside jumped up and ran inside to the cafeteria
    cafeteria_to_outside = 3  # 3 of the students in the cafeteria went outside to see what all the fuss was about

    # Calculate the total number of students in the cafeteria
    total_cafeteria_students = cafeteria_students + outside_to_cafeteria - cafeteria_to_outside
    result = total_cafeteria_students
    return result

print(solution())
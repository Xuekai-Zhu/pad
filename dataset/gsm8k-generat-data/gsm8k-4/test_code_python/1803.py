def solution():
    """There are 90 students who have lunch during period 5. Today, two-thirds of the students sat in the cafeteria, while the remainder sat at the covered picnic tables outside. But some yellow-jackets were attracted to their food, and so one-third of the students outside jumped up and ran inside to the cafeteria, while 3 of the students in the cafeteria went outside to see what all the fuss was about. How many students are now in the cafeteria?"""
    # Define the initial number of students in period 5
    total_students = 90

    # Calculate the number of students in the cafeteria and outside
    cafeteria_students = total_students * (2 / 3)
    outside_students = total_students - cafeteria_students

    # Calculate the number of students who ran inside the cafeteria because of yellow-jackets
    yellow_jackets_students = outside_students / 3

    # Calculate the number of students who went outside from the cafeteria
    gone_out_students = 3

    # Update the number of students in the cafeteria after accounting for the movement
    final_cafeteria_students = cafeteria_students + yellow_jackets_students - gone_out_students

    result = final_cafeteria_students
    return result

print(solution())
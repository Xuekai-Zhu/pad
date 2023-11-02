def solution():
    total_students = 60  # Mr. Sanchez has 60 students in Grade 5
    percent_below_B = 40  # 40% of students got a final grade below B

    # Calculate the number of students who got a final grade of B and above
    above_B = total_students - (total_students * percent_below_B / 100)
    result = above_B
    return result

print(solution())
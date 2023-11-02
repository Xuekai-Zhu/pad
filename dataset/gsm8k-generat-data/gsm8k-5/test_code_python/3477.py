def solution():
    volunteers_from_math_classes = 5 * 6  # 5 students from each of the 6 math classes
    total_volunteers = volunteers_from_math_classes + 13  # 13 teachers have also volunteered

    # Calculate the number of volunteers Mr. Johnson still needs
    volunteers_needed = 50 - total_volunteers
    result = volunteers_needed
    return result

print(solution())
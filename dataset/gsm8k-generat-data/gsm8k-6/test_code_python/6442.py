def solution():
    # Calculate the total number of hot dog buns bought by Mr. Gates
    total_buns = 30 * 8  # 30 packages of hot dog buns, each with 8 buns

    # Calculate the number of hot dog buns per student
    buns_per_student = total_buns / (4 * 30)  # 4 classes with 30 students in each class

    result = buns_per_student
    return result

print(solution())
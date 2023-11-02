def solution():
    num_buns_per_package = 8  # Hot dog buns come in packages of 8
    num_packages = 30  # Mr. Gates bought 30 packages of hot dog buns
    num_classes = 4  # Mr. Gates has 4 classes
    num_students_per_class = 30  # Each of Mr. Gates' classes has 30 students

    # Calculate the total number of hot dog buns
    total_num_buns = num_buns_per_package * num_packages

    # Calculate the number of hot dog buns each student can get
    num_buns_per_student = total_num_buns / (num_classes * num_students_per_class)
    result = num_buns_per_student
    return result

print(solution())
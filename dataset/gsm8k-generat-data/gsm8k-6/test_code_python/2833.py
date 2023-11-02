def solution():
    # Calculate the number of students in each class who prefer goldfish
    students_in_class = 30
    goldfish_in_Johnson = (1/6) * students_in_class
    goldfish_in_Feldstein = (2/3) * students_in_class
    goldfish_in_Henderson = (1/5) * students_in_class

    # Calculate the total number of students who prefer goldfish
    total_goldfish = goldfish_in_Johnson + goldfish_in_Feldstein + goldfish_in_Henderson
    result = total_goldfish
    return result

print(solution())
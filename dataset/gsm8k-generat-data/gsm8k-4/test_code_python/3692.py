def solution():
    """Three different 6th grade classes are combining for a square dancing unit.  If possible, the teachers would like each male student to partner with a female student for the unit.  The first class has 17 males and 13 females, while the second class has 14 males and 18 females, and the third class has 15 males and 17 females.  When the classes are combined, how many students will be unable to partner with a student of the opposite gender?"""
    # Define the number of male and female students in each class
    class1_male = 17
    class1_female = 13
    class2_male = 14
    class2_female = 18
    class3_male = 15
    class3_female = 17

    # Calculate the total number of male and female students
    total_male = class1_male + class2_male + class3_male
    total_female = class1_female + class2_female + class3_female

    # Calculate the number of students unable to partner with a student of the opposite gender
    unable_to_partner = abs(total_male - total_female)

    # Return the result
    result = unable_to_partner
    return result

print(solution())
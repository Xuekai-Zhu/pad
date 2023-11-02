def solution():
    num_students = 20
    num_classes = 3

    # Calculate the number of boys in the school
    num_boys = 0.5 * num_students

    # Calculate the number of girls in the first class
    num_girls_class1 = 15

    # Calculate the number of girls in the second class
    num_girls_class2 = 12

    # Calculate the number of boys in the first class
    num_boys_class1 = num_girls_class1 * num_boys

    # Calculate the number of boys in the second class
    num_boys_class2 = num_girls_class2 * num_boys

    # Calculate the number of boys in the third class
    num_boys_class3 = num_girls_class3 - num_boys_class1
    result = num_boys_class3
    return result

print(solution())
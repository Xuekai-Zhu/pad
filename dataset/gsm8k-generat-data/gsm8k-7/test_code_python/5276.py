def solution():
    original_class_size = 20
    original_girls_percentage = 0.4
    new_boys_added = 5

    # Calculate the number of original girls in the class
    original_girls = int(original_class_size * original_girls_percentage)

    # Calculate the number of original boys in the class
    original_boys = original_class_size - original_girls

    # Calculate the new total number of students
    new_total_students = original_class_size + new_boys_added

    # Calculate the new number of boys in the class
    new_boys = original_boys + new_boys_added

    # Calculate the new number of girls in the class
    new_girls = new_total_students - new_boys

    # Calculate the new percentage of girls in the class
    new_girls_percentage = new_girls / new_total_students

    result = new_girls_percentage
    return result

print(solution())
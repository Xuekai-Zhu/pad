def solution():
    """A 20 person classroom is filled with 40% girls. If 5 new boys join the classroom, what is the new percentage of girls in the class?"""
    # Define the initial number of girls in the classroom
    initial_girls = int(20 * 0.4)

    # Define the initial number of boys in the classroom
    initial_boys = 20 - initial_girls

    # Define the new number of boys in the classroom after 5 new boys join
    new_boys = initial_boys + 5

    # Define the new total number of students in the classroom
    new_total_students = 20 + 5

    # Calculate the new percentage of girls in the classroom
    new_girls_percentage = round((initial_girls / new_total_students) * 100, 2)

    # Display the new percentage of girls
    result = new_girls_percentage
    return result

print(solution())
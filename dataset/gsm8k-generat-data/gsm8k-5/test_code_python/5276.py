def solution():
    # Calculate the number of girls in the classroom
    initial_girls = 20 * 0.4  # 40% of 20-person classroom

    # Calculate the number of boys in the classroom
    initial_boys = 20 - initial_girls

    # Add 5 new boys to the classroom
    new_boys = initial_boys + 5

    # Calculate the new total number of students in the classroom
    new_total = initial_girls + new_boys

    # Calculate the new percentage of girls in the classroom
    new_percentage = (initial_girls / new_total) * 100
    result = new_percentage
    return result

print(solution())
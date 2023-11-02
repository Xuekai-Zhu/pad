def solution():
    """A 20 person classroom is filled with 40% girls. If 5 new boys join the classroom, what is the new percentage of girls in the class?"""
    # Define the initial variables
    total_students = 20
    girls_percent = 40
    boys_percent = 100 - girls_percent

    # Calculate the number of girls and boys in the classroom
    girls = total_students * (girls_percent / 100)
    boys = total_students - girls

    # Add 5 new boys to the classroom
    boys += 5
    total_students += 5

    # Calculate the new percentage of girls in the classroom
    girls_percent_new = (girls / total_students) * 100

    # Return the result
    result = girls_percent_new
    return result

print(solution())
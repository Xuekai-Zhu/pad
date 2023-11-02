def solution():
    """At the beginning of an academic year, there were 15 boys in a class and the number of girls was 20% greater. Later in the year, transfer students were admitted such that the number of girls doubled but the number of boys remained the same. How many students are in the class now?"""
 
    # Define the initial number of boys in the class
    initial_boys = 15

    # Calculate the initial number of girls in the class
    initial_girls = int(initial_boys * 1.2)

    # Calculate the total number of students at the beginning of the year
    total_students = initial_boys + initial_girls

    # Calculate the final number of girls in the class after transfer students were admitted
    final_girls = initial_girls * 2

    # Calculate the total number of students after transfer students were admitted
    total_students += final_girls - initial_girls

    # Return the result
    result = total_students
    return result

print(solution())
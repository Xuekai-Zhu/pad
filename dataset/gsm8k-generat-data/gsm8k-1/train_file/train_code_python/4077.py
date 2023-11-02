def solution():
    """At the beginning of an academic year, there were 15 boys in a class and the number of girls was 20% greater. Later in the year, transfer students were admitted such that the number of girls doubled but the number of boys remained the same. How many students are in the class now?"""
    initial_boys = 15
    initial_girls = int(initial_boys * 1.2)
    new_girls = initial_girls * 2
    new_students = new_girls + initial_boys
    result = new_students
    return result

print(solution())
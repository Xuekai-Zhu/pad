def solution():
    num_boys = 12
    num_girls = 12

    # Calculate the number of girls who are on varsity
    num_varsity_boys = num_boys / 3

    # Calculate the number of boys who are not on varsity
    num_non_varsity_boys = num_boys - num_varsity_boys

    # Calculate the number of students who are not on varsity
    num_non_varsity_students = num_non_varsity_boys + num_non_varsity_girls
    result = num_non_varsity_students
    return result

print(solution())
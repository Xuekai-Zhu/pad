def solution():
    total_children = 45
    girls_fraction = 1/3

    # Calculate the number of girls in the classroom
    num_girls = total_children * girls_fraction

    # Calculate the number of boys in the classroom
    num_boys = total_children - num_girls
    result = num_boys
    return result

print(solution())
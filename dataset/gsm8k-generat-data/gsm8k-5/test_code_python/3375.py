def solution():
    # Calculate the number of girls in the school
    num_girls = 0.6 * 150

    # Calculate the number of boys in the school
    num_boys = 150 - num_girls

    # Calculate the number of boys who joined varsity clubs
    varsity_boys = (1/3) * num_boys

    # Calculate the number of boys who did not join varsity clubs
    non_varsity_boys = num_boys - varsity_boys
    result = non_varsity_boys
    return result

print(solution())
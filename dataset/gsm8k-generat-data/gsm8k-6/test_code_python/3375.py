def solution():
    # Calculate the number of girls and boys in the school
    num_girls = 0.6 * 150
    num_boys = 150 - num_girls

    # Calculate the number of boys who joined varsity clubs
    joined = 1/3 * num_boys

    # Calculate the number of boys who did not join varsity clubs
    not_joined = num_boys - joined
    result = not_joined
    return result

print(solution())
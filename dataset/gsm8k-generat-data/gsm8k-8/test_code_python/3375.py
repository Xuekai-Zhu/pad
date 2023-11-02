def solution():
    # Calculate the number of girls
    num_girls = 0.6 * 150

    # Calculate the number of boys
    num_boys = 150 - num_girls

    # Calculate the number of boys who joined varsity clubs
    num_boys_in_clubs = (1/3) * num_boys

    # Calculate the number of boys who did not join varsity clubs
    num_boys_not_in_clubs = num_boys - num_boys_in_clubs

    result = num_boys_not_in_clubs
    return result

print(solution())
def solution():
    # Calculate the number of girls and boys in the class
    num_girls = 0.6 * 25
    num_boys = 25 - num_girls

    # Calculate the number of boys who like basketball and those who don't
    boys_play_basketball = 0.4 * num_boys
    boys_dont_play_basketball = num_boys - boys_play_basketball

    # Calculate the number of girls who like playing basketball
    girls_play_basketball = 2 * boys_dont_play_basketball

    # Calculate the percentage of girls who like playing basketball
    percent_girls_play_basketball = (girls_play_basketball / num_girls) * 100

    result = percent_girls_play_basketball
    return result

print(solution())
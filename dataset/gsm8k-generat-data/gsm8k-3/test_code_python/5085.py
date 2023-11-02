def solution():
    """Salem is 15 times the size of Leesburg. Leesburg has 58940 people. If 130000 people move out of Salem, and half of Salem's population is women, how many women live in Salem?"""
    # Define the population of Leesburg and the ratio of Salem to Leesburg
    leesburg_pop = 58940
    salem_leesburg_ratio = 15

    # Calculate the population of Salem
    salem_pop = salem_leesburg_ratio * leesburg_pop

    # Calculate the new population of Salem after 130000 people move out
    salem_pop -= 130000

    # Calculate the number of women in Salem
    women_pop = salem_pop / 2

    # Display the number of women in Salem
    result = women_pop
    return result

print(solution())
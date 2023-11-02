def solution():
    # Calculate the percentage of male turtles
    male_percentage = 100 - 60
    male_fraction = male_percentage / 100

    # Calculate the number of male turtles
    total_turtles = 1 / male_fraction

    # Calculate the number of male turtles with stripes
    stripes_fraction = 1 / 4
    stripes_male = total_turtles * male_fraction * stripes_fraction

    # Calculate the number of adult turtles with stripes
    stripes_adult = 0.6 * stripes_male

    # Calculate the total number of turtles
    total_female = 0.6 * total_turtles
    total_adult = total_turtles - total_female
    total_babies = stripes_male - stripes_adult
    total_turtles = total_female + total_adult + total_babies

    result = total_turtles
    return result

print(solution())
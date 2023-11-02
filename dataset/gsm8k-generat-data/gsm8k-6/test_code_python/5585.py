def solution():
    # Calculate the total number of times animals were seen in the first 3 months of the year
    jan_animals = 26  # number of times animals were seen in January
    feb_animals = 3 * jan_animals  # number of times animals were seen in February
    mar_animals = feb_animals / 2  # number of times animals were seen in March
    total_animals = jan_animals + feb_animals + mar_animals  # total number of times animals were seen in the first 3 months of the year
    result = total_animals
    return result

print(solution())
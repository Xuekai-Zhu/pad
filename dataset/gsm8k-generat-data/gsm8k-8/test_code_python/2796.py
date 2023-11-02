def solution():
    # Calculate the number of Julian's friends who are boys and girls
    julian_boys = 0.6 * 80
    julian_girls = 0.4 * 80

    # Calculate the number of Boyd's friends who are girls
    boyd_girls = (1/3) * 100

    # Calculate the number of Boyd's friends who are boys
    boyd_boys = 100 - boyd_girls

    # Calculate the percentage of Boyd's friends who are boys
    boyd_boys_percentage = (boyd_boys / 100) * 100
    result = boyd_boys_percentage
    return result

print(solution())
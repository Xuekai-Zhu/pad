def solution():
    # Calculate the number of packages based on the ratio of packages to meals
    packages = 8 * 27 / 9

    # Calculate the number of meals to deliver
    meals = 27 - packages

    result = meals
    return result

print(solution())
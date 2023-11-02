def solution():
    # Define the number of adults and girls
    adults = 3
    girls = 7

    # Calculate the total number of eggs used by the adults
    adult_eggs = adults * 3

    # Calculate the total number of eggs used by the girls
    girl_eggs = girls * 1

    # Calculate the remaining eggs for the boys
    remaining_eggs = 3 * 12 - adult_eggs - girl_eggs

    # Calculate the number of boys
    boys = remaining_eggs // 2

    result = boys
    return result

print(solution())
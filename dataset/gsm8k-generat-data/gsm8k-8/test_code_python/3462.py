def solution():
    # Define initial number of cats
    initial_cats = 1800

    # Calculate the number of cats relocated on the first mission
    relocated_cats_1 = 600

    # Calculate the number of cats remaining after the first mission
    remaining_cats_1 = initial_cats - relocated_cats_1

    # Calculate the number of cats relocated on the second mission
    relocated_cats_2 = remaining_cats_1 / 2

    # Calculate the number of cats remaining after the second mission
    remaining_cats_2 = remaining_cats_1 - relocated_cats_2

    result = remaining_cats_2
    return result

print(solution())
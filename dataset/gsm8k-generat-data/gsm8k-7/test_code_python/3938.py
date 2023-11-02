def solution():
    num_people = 6
    num_rows = 3
    num_columns = 6

    # Calculate the total number of brownies
    total_brownies = num_rows * num_columns

    # Calculate how many brownies each person can eat
    num_brownies_per_person = total_brownies / num_people
    result = num_brownies_per_person
    return result

print(solution())
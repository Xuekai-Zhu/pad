def solution():
    # Calculate the total number of brownies in the pan
    total_brownies = 6 * 3  # 6 columns and 3 rows

    # Calculate the number of brownies each person can eat
    num_people = 6  # Including Frank
    brownies_per_person = total_brownies / num_people
    result = brownies_per_person
    return result

print(solution())
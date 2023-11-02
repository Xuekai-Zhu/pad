def solution():
    total_eggs = 3 * 12  # There are three dozen eggs
    eggs_per_omelet = 4  # Each omelet requires 4 eggs
    people = 3  # There are 3 people in Pauly's family

    # Calculate the total number of omelets Pauly can make
    total_omelets = total_eggs // eggs_per_omelet

    # Calculate the number of omelets each person gets
    omelets_per_person = total_omelets // people
    result = omelets_per_person
    return result

print(solution())
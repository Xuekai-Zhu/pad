def solution():
    num_eggs = 3*12
    num_people = 3
    eggs_per_omelet = 4

    # Calculate the total number of omelets that can be made
    num_omelets = num_eggs // eggs_per_omelet

    # Calculate the number of omelets each person gets
    num_omelets_per_person = num_omelets // num_people
    result = num_omelets_per_person
    return result

print(solution())
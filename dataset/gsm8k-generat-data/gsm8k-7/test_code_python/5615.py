def solution():
    starting_phones = 15
    fixed_phones = 3
    dropped_off_phones = 6
    coworker_ratio = 0.5

    # Calculate the total number of phones that need to be repaired by Kevin
    total_phones = starting_phones + dropped_off_phones - fixed_phones

    # Calculate the number of phones that the coworker will fix
    coworker_phones = total_phones * coworker_ratio

    # Calculate the number of phones that Kevin will fix
    kevin_phones = total_phones - coworker_phones

    # Calculate how many phones each person will need to repair
    num_phones_per_person = total_phones / 2
    result = num_phones_per_person
    return result

print(solution())
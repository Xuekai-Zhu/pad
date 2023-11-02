def solution():
    starting_phones = 15  # Kevin starts with 15 phones that need to be repaired
    repaired_phones = 3  # Kevin has already repaired 3 phones
    new_phones = 6  # A client brought in 6 more phones to be repaired
    total_phones = starting_phones + new_phones  # Kevin now has a total of 21 phones to repair
    remaining_phones = total_phones - repaired_phones  # Kevin has 18 phones left to repair

    # Calculate how many phones each person will need to repair if the coworker helps
    phones_each = remaining_phones / 2
    result = phones_each
    return result

print(solution())
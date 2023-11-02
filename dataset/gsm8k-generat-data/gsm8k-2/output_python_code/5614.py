def solution():
    """Kevin repairs phones at his job. At the beginning of the day, Kevin has 15 phones that need to be repaired. By the afternoon, Kevin has successfully repaired 3 of the 15 phones and a client has dropped off 6 more phones that need fixing. If a coworker of Kevin's offers to help him and fix half of the damaged phones, how many phones will each person need to repair?"""
    initial_phones = 15
    repaired_phones = 3
    new_phones = 6
    total_phones = initial_phones + new_phones
    remaining_phones = total_phones - repaired_phones
    phones_per_person = remaining_phones / 2
    result = phones_per_person
    return result

print(solution())
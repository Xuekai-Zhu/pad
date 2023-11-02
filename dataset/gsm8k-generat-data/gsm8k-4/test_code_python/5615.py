def solution():
    """Kevin repairs phones at his job. At the beginning of the day, Kevin has 15 phones that need to be repaired. By the afternoon, Kevin has successfully repaired 3 of the 15 phones and a client has dropped off 6 more phones that need fixing. If a coworker of Kevin's offers to help him and fix half of the damaged phones, how many phones will each person need to repair?"""
    # Define the initial number of phones that need to be repaired
    initial_phones = 15

    # Calculate the number of phones that still need to be repaired after Kevin fixes 3 and a client drops off 6
    remaining_phones = initial_phones - 3 + 6

    # Calculate the number of phones that each person needs to repair if Kevin's coworker helps
    phones_per_person = remaining_phones / 2

    result = phones_per_person
    return result

print(solution())
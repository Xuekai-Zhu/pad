def solution():
    """Kevin repairs phones at his job. At the beginning of the day, Kevin has 15 phones that need to be repaired. By the afternoon, Kevin has successfully repaired 3 of the 15 phones and a client has dropped off 6 more phones that need fixing. If a coworker of Kevin's offers to help him and fix half of the damaged phones, how many phones will each person need to repair?"""
    # Define the initial number of phones that need fixing
    initial_phones = 15

    # Calculate the number of phones left after Kevin repaired 3 and received 6 more
    total_phones = initial_phones - 3 + 6

    # Calculate the number of phones each person will need to fix if the coworker helps
    phones_per_person = total_phones / 2

    # Display the number of phones each person will need to fix
    result = phones_per_person
    return result

print(solution())
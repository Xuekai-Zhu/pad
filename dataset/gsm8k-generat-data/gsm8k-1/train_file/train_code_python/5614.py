def solution():
    """Kevin repairs phones at his job. At the beginning of the day, Kevin has 15 phones that need to be repaired. By the afternoon, Kevin has successfully repaired 3 of the 15 phones and a client has dropped off 6 more phones that need fixing. If a coworker of Kevin's offers to help him and fix half of the damaged phones, how many phones will each person need to repair?"""
    total_phones = 15 + 6
    phones_repaired = 3
    phones_left = total_phones - phones_repaired
    phones_each = phones_left / 2
    result = phones_each
    return result

print(solution())
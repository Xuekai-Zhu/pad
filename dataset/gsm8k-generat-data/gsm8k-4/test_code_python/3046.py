def solution():
    """Kekai is running a sundae booth at the carnival. On Monday, he makes a total of 40 sundaes, and he puts 6 m&ms on each sundae. On Tuesday, he makes a total of 20 sundaes, and he puts 10 m&ms on each sundae. If each m&m pack contains 40 m&ms, how many m&m packs does Kekai use?"""
    # Calculate the total number of m&ms used on Monday
    monday_mms = 40 * 6

    # Calculate the total number of m&ms used on Tuesday
    tuesday_mms = 20 * 10

    # Calculate the total number of m&ms used
    total_mms = monday_mms + tuesday_mms

    # Calculate the number of m&m packs used
    mms_per_pack = 40
    packs_used = total_mms // mms_per_pack

    result = packs_used
    return result

print(solution())
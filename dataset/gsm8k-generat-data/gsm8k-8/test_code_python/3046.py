def solution():
    # Calculate the total number of m&ms used on Monday
    monday_mms = 40 * 6

    # Calculate the total number of m&ms used on Tuesday
    tuesday_mms = 20 * 10

    # Calculate the total number of m&ms used
    total_mms = monday_mms + tuesday_mms

    # Calculate the number of m&m packs used
    mms_per_pack = 40
    mms_packs_used = total_mms // mms_per_pack

    result = mms_packs_used
    return result

print(solution())
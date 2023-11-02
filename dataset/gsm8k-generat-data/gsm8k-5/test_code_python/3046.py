def solution():
    # Calculate the total number of m&ms used on Monday
    mms_monday = 40 * 6  # 6 m&ms on each of the 40 sundaes

    # Calculate the total number of m&ms used on Tuesday
    mms_tuesday = 20 * 10  # 10 m&ms on each of the 20 sundaes

    # Calculate the total number of m&ms used in both days
    total_mms = mms_monday + mms_tuesday

    # Calculate the number of m&m packs used
    mms_per_pack = 40  # Each pack contains 40 m&ms
    mms_packs = total_mms / mms_per_pack

    result = mms_packs
    return result

print(solution())
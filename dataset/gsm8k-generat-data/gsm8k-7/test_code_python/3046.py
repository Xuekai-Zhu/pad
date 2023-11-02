def solution():
    monday_sundaes = 40
    monday_mms_per_sundae = 6
    tuesday_sundaes = 20
    tuesday_mms_per_sundae = 10
    mms_per_pack = 40

    # Calculate the total number of m&ms used on Monday
    monday_mms_used = monday_sundaes * monday_mms_per_sundae

    # Calculate the total number of m&ms used on Tuesday
    tuesday_mms_used = tuesday_sundaes * tuesday_mms_per_sundae

    # Calculate the total number of m&m packs used
    total_mms_used = monday_mms_used + tuesday_mms_used
    num_mms_packs = total_mms_used / mms_per_pack
    result = num_mms_packs
    return result

print(solution())
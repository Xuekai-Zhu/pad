def solution():
    # Calculate the total number of m&ms used by Kekai on Monday and Tuesday
    mms_on_Monday = 6 * 40  # 6 m&ms on each of the 40 sundaes made on Monday 
    mms_on_Tuesday = 10 * 20  # 10 m&ms on each of the 20 sundaes made on Tuesday
    total_mms = mms_on_Monday + mms_on_Tuesday  # total number of m&ms used

    # Calculate the number of m&m packs used
    mms_per_pack = 40
    mms_packs = total_mms / mms_per_pack
    result = mms_packs
    return result

print(solution())
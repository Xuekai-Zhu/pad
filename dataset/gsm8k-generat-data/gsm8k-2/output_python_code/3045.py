def solution():
    """Kekai is running a sundae booth at the carnival. On Monday, he makes a total of 40 sundaes, and he puts 6 m&ms on each sundae. On Tuesday, he makes a total of 20 sundaes, and he puts 10 m&ms on each sundae. If each m&m pack contains 40 m&ms, how many m&m packs does Kekai use?"""
    monday_sundaes = 40
    monday_mms_per_sundae = 6
    tuesday_sundaes = 20
    tuesday_mms_per_sundae = 10
    total_mms = (monday_sundaes * monday_mms_per_sundae) + (tuesday_sundaes * tuesday_mms_per_sundae)
    mms_per_pack = 40
    total_packs = total_mms // mms_per_pack
    if total_mms % mms_per_pack != 0:
        total_packs += 1
    result = total_packs
    return result

print(solution())
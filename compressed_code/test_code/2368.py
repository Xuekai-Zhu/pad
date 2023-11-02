def solution():
    
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
def solution():
    
    bald_mtn_snow = 1.5
    billy_mtn_snow = 3.5
    mount_pilot_snow = 1.26
    total_billy_pilot_snow = (billy_mtn_snow * 100) + (mount_pilot_snow * 1e2)
    total_bald_snow = bald_mtn_snow * 1e2
    difference = total_billy_pilot_snow - total_bald_snow
    result = difference
    return result

print(solution())
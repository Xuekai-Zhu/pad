def solution():
    centimeters = 100
    meters = 1
    bald_mountain_snow = 1.5 * meters
    billy_mountain_snow = 3.5 * meters
    mount_pilot_snow = 126 * centimeters
    total_snow = bald_mountain_snow + billy_mountain_snow + mount_pilot_snow
    result = total_snow - bald_mountain_snow
    return result

print(solution())
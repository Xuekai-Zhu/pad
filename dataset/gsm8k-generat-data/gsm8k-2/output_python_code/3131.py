def solution():
    """Bald Mountain received 1.5 meters of snow last week. During a blizzard, Billy Mountain received 3.5 meters of snow and Mount Pilot received 126 centimeters of snow. How many more centimeters of snow did Billy Mountain and Mount Pilot have then Bald Mountain?"""
    bald_mtn_snow = 1.5
    billy_mtn_snow = 3.5
    mount_pilot_snow = 1.26
    total_billy_pilot_snow = (billy_mtn_snow * 100) + (mount_pilot_snow * 1e2)
    total_bald_snow = bald_mtn_snow * 1e2
    difference = total_billy_pilot_snow - total_bald_snow
    result = difference
    return result

print(solution())
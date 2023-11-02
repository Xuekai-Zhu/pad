def solution():
    """Bald Mountain received 1.5 meters of snow last week. During a blizzard, Billy Mountain received 3.5 meters of snow and Mount Pilot received 126 centimeters of snow. How many more centimeters of snow did Billy Mountain and Mount Pilot have then Bald Mountain?"""
    # Define the amount of snow received by Bald Mountain in centimeters
    bald_mountain_snow_cm = 150

    # Calculate the amount of snow received by Billy Mountain in centimeters
    billy_mountain_snow_cm = 350

    # Calculate the amount of snow received by Mount Pilot in centimeters
    mount_pilot_snow_cm = 126

    # Calculate the difference in snow between Bald Mountain and Billy Mountain in centimeters
    diff_bald_billy_cm = billy_mountain_snow_cm - bald_mountain_snow_cm

    # Calculate the difference in snow between Bald Mountain and Mount Pilot in centimeters
    diff_bald_pilot_cm = mount_pilot_snow_cm - bald_mountain_snow_cm

    # Calculate the total difference in snow between Billy Mountain and Mount Pilot in centimeters
    total_diff_cm = diff_bald_billy_cm + diff_bald_pilot_cm

    # return the result
    result = total_diff_cm
    return result

print(solution())
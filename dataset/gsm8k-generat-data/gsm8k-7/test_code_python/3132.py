def solution():
    bald_mtn_snow = 1.5 # meters
    billy_mtn_snow = 3.5 # meters
    mount_pilot_snow = 1.26 # meters

    # Convert Bald Mountain's snowfall to centimeters
    bald_mtn_snow_cm = bald_mtn_snow * 100

    # Convert Billy Mountain's snowfall to centimeters
    billy_mtn_snow_cm = billy_mtn_snow * 100

    # Convert Mount Pilot's snowfall to centimeters
    mount_pilot_snow_cm = mount_pilot_snow * 100

    # Calculate the difference in snowfall between Billy Mountain and Bald Mountain
    billy_mtn_diff = billy_mtn_snow_cm - bald_mtn_snow_cm

    # Calculate the difference in snowfall between Mount Pilot and Bald Mountain
    mount_pilot_diff = mount_pilot_snow_cm - bald_mtn_snow_cm

    # Calculate the total difference in snowfall between Billy Mountain and Mount Pilot
    total_diff = billy_mtn_diff + mount_pilot_diff
    result = total_diff
    return result

print(solution())
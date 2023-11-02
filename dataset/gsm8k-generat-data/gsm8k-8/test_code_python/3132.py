def solution():
    # Convert Bald Mountain's snowfall to centimeters
    bald_mtn_snow = 1.5 * 100

    # Convert Billy Mountain's snowfall to centimeters
    billy_mtn_snow = 3.5 * 100

    # Convert Mount Pilot's snowfall to centimeters
    mount_pilot_snow = 126

    # Calculate the difference in snowfall between Billy and Bald Mountains
    billy_mtn_diff = billy_mtn_snow - bald_mtn_snow

    # Calculate the difference in snowfall between Mount Pilot and Bald Mountain
    mount_pilot_diff = mount_pilot_snow - bald_mtn_snow

    # Calculate the total difference in snowfall between both mountains
    total_diff = billy_mtn_diff + mount_pilot_diff

    result = total_diff
    return result

print(solution())
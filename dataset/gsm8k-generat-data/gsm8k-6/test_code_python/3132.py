def solution():
    # Convert snowfall measurements to centimeters
    bald_mtn_snow = 1.5 * 100  # 1 meter = 100 centimeters
    billy_mtn_snow = 3.5 * 100
    mount_pilot_snow = 126

    # Calculate the difference in snowfall between each mountain and Bald Mountain
    billy_diff = billy_mtn_snow - bald_mtn_snow
    pilot_diff = mount_pilot_snow - bald_mtn_snow

    # Convert the difference in snowfall back to meters
    total_diff = (billy_diff + pilot_diff) / 100

    result = total_diff
    return result

print(solution())
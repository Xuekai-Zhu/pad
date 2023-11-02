def solution():
    bald_mountain_snow = 1.5  # Bald Mountain received 1.5 meters of snow
    billy_mountain_snow = 3.5  # Billy Mountain received 3.5 meters of snow
    mount_pilot_snow = 1.26  # Mount Pilot received 126 centimeters of snow

    # Convert Bald Mountain's snow to centimeters
    bald_mountain_snow_cm = bald_mountain_snow * 100

    # Convert Billy Mountain's snow to centimeters
    billy_mountain_snow_cm = billy_mountain_snow * 100

    # Calculate the total snow in centimeters for Bald Mountain and compare with Billy Mountain and Mount Pilot
    total_diff = (billy_mountain_snow_cm + mount_pilot_snow) - bald_mountain_snow_cm
    result = total_diff
    return result

print(solution())
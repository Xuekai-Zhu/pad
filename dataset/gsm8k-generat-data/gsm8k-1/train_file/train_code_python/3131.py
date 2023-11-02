def solution():
    """Bald Mountain received 1.5 meters of snow last week. During a blizzard, Billy Mountain received 3.5 meters of snow and Mount Pilot received 126 centimeters of snow. How many more centimeters of snow did Billy Mountain and Mount Pilot have then Bald Mountain?"""
    bald_mountain = 1.5 * 100  # Convert meters to centimeters
    billy_mountain = 3.5 * 100  # Convert meters to centimeters
    mount_pilot = 126
    total_mountain_snow = billy_mountain + mount_pilot
    more_snow = total_mountain_snow - bald_mountain
    result = more_snow
    return result

print(solution())
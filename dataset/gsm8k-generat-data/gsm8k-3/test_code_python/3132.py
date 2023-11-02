def solution():
    """Bald Mountain received 1.5 meters of snow last week. During a blizzard, Billy Mountain received 3.5 meters of snow and Mount Pilot received 126 centimeters of snow. How many more centimeters of snow did Billy Mountain and Mount Pilot have then Bald Mountain?"""
    # Convert all units to centimeters
    bald_mountain_snow = 1.5 * 100
    billy_mountain_snow = 3.5 * 100
    mount_pilot_snow = 126

    # Calculate the difference in snow between Bald Mountain and Billy Mountain
    difference_bald_billy = billy_mountain_snow - bald_mountain_snow

    # Calculate the difference in snow between Bald Mountain and Mount Pilot
    difference_bald_pilot = mount_pilot_snow - bald_mountain_snow

    # Calculate the total difference in snow
    total_difference = difference_bald_billy + difference_bald_pilot

    # Display the total difference in snow
    result = total_difference
    return result

print(solution())
def solution():
    building_height = 20  # The building has 20 stories
    lola_speed = 10  # Lola runs up 1 story in 10 seconds
    tara_speed = (8 + 3)  # Tara's elevator takes 8 seconds to go up a story and it stops for 3 seconds on every floor

    # Calculate the time it takes for Lola to reach the top
    lola_time = lola_speed * building_height

    # Calculate the time it takes for Tara to reach the top
    tara_time = tara_speed * building_height

    # Determine the slower time
    slower_time = max(lola_time, tara_time)
    result = slower_time
    return result

print(solution())
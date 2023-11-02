def solution():
    """Keanu was surfing towards the shore at a speed of 20 miles per hour.  A shark was swimming alongside him, riding the same wave, when it doubled its speed and moved away from Keanu.  There was a pilot fish swimming alongside Keanu and the shark, and when the shark increased its speed, the pilot fish also increased its speed and moved away from Keanu, but only increasing its speed by half as much as the shark had increased its speed by.  What speed, in miles per hour, was the pilot fish swimming when it moved away from Keanu?"""
    # Define Keanu's speed
    keanu_speed = 20

    # Define the shark's initial speed and final speed
    shark_initial_speed = keanu_speed
    shark_final_speed = shark_initial_speed * 2

    # Define the pilot fish's initial speed and final speed
    pilot_fish_initial_speed = keanu_speed
    pilot_fish_final_speed = pilot_fish_initial_speed + (shark_final_speed - shark_initial_speed) / 2

    result = pilot_fish_final_speed
    return result

print(solution())
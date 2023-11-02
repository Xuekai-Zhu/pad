def solution():
    # Define the initial speed of Keanu, the shark, and the pilot fish
    keanu_speed = 20
    shark_speed = keanu_speed * 2

    # Calculate the increase in speed for the pilot fish
    shark_speed_increase = shark_speed - keanu_speed
    pilot_fish_speed_increase = shark_speed_increase / 2

    # Calculate the final speed of the pilot fish
    pilot_fish_speed = keanu_speed + pilot_fish_speed_increase
    result = pilot_fish_speed
    return result

print(solution())
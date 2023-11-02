def solution():
    keanu_speed = 20  # Keanu's speed is 20 miles per hour
    shark_speed = keanu_speed * 2  # Shark's speed is double of Keanu's speed
    pilot_fish_increase = (shark_speed - keanu_speed) / 2  # Pilot fish increases its speed by half of the shark's increase
    pilot_fish_speed = keanu_speed + pilot_fish_increase  # Calculate the speed of the pilot fish

    result = pilot_fish_speed
    return result

print(solution())
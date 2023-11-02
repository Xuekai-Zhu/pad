def solution():
    keanu_speed = 20  # Keanu's speed
    shark_speed = keanu_speed * 2  # Shark's speed after doubling its speed
    pilot_fish_speed = keanu_speed + (shark_speed - keanu_speed) * 0.5  # Pilot fish's speed after increasing speed by half of the shark's increment

    result = pilot_fish_speed
    return result

print(solution())
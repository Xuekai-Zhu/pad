def solution():
    """Keanu was surfing towards the shore at a speed of 20 miles per hour. A shark was swimming alongside him, riding the same wave, when it doubled its speed and moved away from Keanu. There was a pilot fish swimming alongside Keanu and the shark, and when the shark increased its speed, the pilot fish also increased its speed and moved away from Keanu, but only increasing its speed by half as much as the shark had increased its speed by. What speed, in miles per hour, was the pilot fish swimming when it moved away from Keanu?"""
    keanu_speed = 20
    shark_speed = keanu_speed * 2
    pilot_fish_speed_increase = (shark_speed - keanu_speed) / 2
    pilot_fish_speed = keanu_speed + pilot_fish_speed_increase
    result = pilot_fish_speed
    return result

print(solution())
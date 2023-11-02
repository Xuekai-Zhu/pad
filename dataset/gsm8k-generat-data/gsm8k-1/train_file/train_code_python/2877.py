def solution():
    """Noah’s bedroom light uses 6 watts per hour. His office light is much brighter so he can see to work and uses three times as much energy. The living room light has a much larger space to cover and has to be more powerful, so it uses four times as much energy as his bedroom light. If Noah leaves all those lights on for two hours, how many watts has he used?"""
    bedroom_light = 6
    office_light = bedroom_light * 3
    living_room_light = bedroom_light * 4
    total_watts = (bedroom_light + office_light + living_room_light) * 2
    result = total_watts
    return result

print(solution())
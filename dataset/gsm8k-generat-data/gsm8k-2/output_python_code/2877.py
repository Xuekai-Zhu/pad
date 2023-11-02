def solution():
    """Noah’s bedroom light uses 6 watts per hour. His office light is much brighter so he can see to work and uses three times as much energy. The living room light has a much larger space to cover and has to be more powerful, so it uses four times as much energy as his bedroom light. If Noah leaves all those lights on for two hours, how many watts has he used?"""
    bedroom_light_watt = 6
    office_light_watt = 3 * bedroom_light_watt
    living_room_light_watt = 4 * bedroom_light_watt
    total_watts = (bedroom_light_watt + office_light_watt + living_room_light_watt) * 2
    result = total_watts
    return result

print(solution())
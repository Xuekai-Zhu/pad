def solution():
    """Noah’s bedroom light uses 6 watts per hour. His office light is much brighter so he can see to work and uses three times as much energy. The living room light has a much larger space to cover and has to be more powerful, so it uses four times as much energy as his bedroom light. If Noah leaves all those lights on for two hours, how many watts has he used?"""
    # Define the energy usage of each light in watts per hour
    BEDROOM_LIGHT = 6
    OFFICE_LIGHT = BEDROOM_LIGHT * 3
    LIVING_ROOM_LIGHT = BEDROOM_LIGHT * 4

    # Define the number of hours the lights are left on
    hours = 2

    # Calculate the total energy usage in watts for the given time period
    total_energy_usage = (BEDROOM_LIGHT + OFFICE_LIGHT + LIVING_ROOM_LIGHT) * hours

    # Display the total energy usage in watts
    result = total_energy_usage
    return result

print(solution())
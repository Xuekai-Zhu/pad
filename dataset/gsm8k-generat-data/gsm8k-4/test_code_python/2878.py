def solution():
    """Noah’s bedroom light uses 6 watts per hour. His office light is much brighter so he can see to work and 
    uses three times as much energy. The living room light has a much larger space to cover and has to be 
    more powerful, so it uses four times as much energy as his bedroom light. 
    If Noah leaves all those lights on for two hours, how many watts has he used?"""
    
    # Define the wattage of the bedroom light
    bedroom_wattage = 6
    
    # Define the wattage of the office light
    office_wattage = bedroom_wattage * 3
    
    # Define the wattage of the living room light
    livingroom_wattage = bedroom_wattage * 4
    
    # Calculate the total wattage used in two hours
    total_wattage = (bedroom_wattage + office_wattage + livingroom_wattage) * 2
    
    result = total_wattage
    return result

print(solution())
def solution():
    """Hani said she would do 3 more situps per minute than Diana would. Diana then did 40 situps at a rate of 4 situps per minute. Calculate the total number of situps they did together."""
    # Calculate the rate at which Hani did the situps
    hani_rate = 4 + 3
    
    # Calculate the number of situps Hani did
    hani_situps = hani_rate * 40 / 4
    
    # Calculate the total number of situps
    total_situps = hani_situps + 40
    
    # Display the total number of situps
    result = total_situps
    return result

print(solution())
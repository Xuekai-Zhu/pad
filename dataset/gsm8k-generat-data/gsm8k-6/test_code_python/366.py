def solution():
    # Calculate the total length of the ladder climbed by Keaton
    keaton_length = 30 * 20  # Keaton climbed a 30 feet ladder twenty times
    
    # Calculate the length of the ladder climbed by Reece
    reece_length = (30 - 4) * 15  # Reece climbed a ladder 4 feet shorter than Keaton's ladder 15 times
    
    # Convert the total length to inches
    total_length = (keaton_length + reece_length) * 12  # 1 foot equals 12 inches
    
    result = total_length
    return result

print(solution())
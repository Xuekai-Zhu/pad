def solution():
    """Adam really wants to ride the biggest roller coaster at the park. You have to be 4 feet tall to ride it. Adam’s height is 40 inches and he grows 2 inches a year. How many years until he is tall enough to ride it?"""
    required_height = 4 * 12  # converting to inches
    current_height = 40
    growth_rate = 2
    years_to_reach_height = (required_height - current_height) / growth_rate
    result = years_to_reach_height
    
    return result

print(solution())
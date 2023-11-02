def solution():
    # Calculate the total amount of water needed for the team
    total_water_needed = 0.2 * 30  # 200 milliliters of water for every player
    remaining_water = 8 - (total_water_needed + 0.25)  # subtract the spilled water from the total amount of water left with the coach
    
    result = remaining_water
    return result

print(solution())
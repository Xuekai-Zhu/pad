def solution():
    full_ladder_steps = 11  # Darry's full ladder has 11 steps
    full_ladder_climbs = 10  # Darry climbed his full ladder 10 times today
    smaller_ladder_steps = 6  # Darry's smaller ladder has 6 steps
    smaller_ladder_climbs = 7  # Darry climbed his smaller ladder 7 times today

    # Calculate the total number of steps Darry climbed today
    total_steps = full_ladder_steps * full_ladder_climbs + smaller_ladder_steps * smaller_ladder_climbs
    result = total_steps
    return result

print(solution())
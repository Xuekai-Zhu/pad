def solution():
    # Calculate the total number of balloons after additions
    total_balloons = 12 + 8 + 6 + 24  # Brooke adds 8 to his current 12, Tracy adds 24 to her current 6
    # Calculate how many balloons Tracy has left after popping half
    tracy_remaining_balloons = (1/2) * (6 + 24) # Half of Tracy's total balloons
    # Calculate the final total number of balloons
    final_total = total_balloons - (24 - tracy_remaining_balloons)
    result = final_total
    return result

print(solution())
def solution():
    # Calculate the total yards of fabric needed for the shirts and pants made in a day
    total_fabric_per_day = 3 * 2 + 5 * 5  # Jenson makes 3 shirts and Kingsley makes 5 pairs of pants
    # Calculate the total yards of fabric needed for 3 days
    total_fabric_for_3_days = total_fabric_per_day * 3
    result = total_fabric_for_3_days
    return result

print(solution())
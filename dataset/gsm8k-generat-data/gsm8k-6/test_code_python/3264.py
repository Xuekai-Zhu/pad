def solution():
    # Calculate the total length of ribbon needed
    total_ribbon = 8 * 1.5  # each gift requires 1.5 meters of ribbon

    # Calculate the length of ribbon left
    ribbon_left = 15 - total_ribbon
    result = ribbon_left
    return result

print(solution())
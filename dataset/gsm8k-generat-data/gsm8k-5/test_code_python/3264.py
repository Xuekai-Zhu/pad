def solution():
    num_gifts = 8  # Sammy has 8 gifts to wrap
    ribbon_per_gift = 1.5  # Each gift requires 1.5 meters of ribbon
    total_ribbon_needed = num_gifts * ribbon_per_gift  # Total length of ribbon needed

    tom_ribbon_length = 15  # Tom has a 15-meter long ribbon
    ribbon_left = tom_ribbon_length - total_ribbon_needed  # Length of ribbon left after wrapping all gifts

    result = ribbon_left
    return result

print(solution())
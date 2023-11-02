def solution():
    gray_whale_length = 4.9 # measured in meters
    semi_trailer_length = 48 # measured in feet
    # Convert gray whale length to feet
    gray_whale_length_in_feet = gray_whale_length * 3.281
    if gray_whale_length_in_feet <= semi_trailer_length:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
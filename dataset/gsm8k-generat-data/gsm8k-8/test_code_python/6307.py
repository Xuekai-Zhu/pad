def solution():
    # Define total length of show and length of commercials
    total_length = 1.5
    commercial_length = 3 * 10 / 60

    # Calculate length of show without commercials
    show_length = total_length - commercial_length
    result = show_length
    return result

print(solution())
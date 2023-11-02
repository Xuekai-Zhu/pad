def solution():
    pink_hangers = 7  # Fifi has 7 pink hangers
    green_hangers = 4  # Fifi has 4 green hangers
    blue_hangers = green_hangers - 1  # Fifi has one less blue hanger than green hangers
    yellow_hangers = blue_hangers - 1  # Fifi has one less yellow hanger than blue hangers

    # Calculate the total number of colored hangers
    total_hangers = pink_hangers + green_hangers + blue_hangers + yellow_hangers
    result = total_hangers
    return result

print(solution())
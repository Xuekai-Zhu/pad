def solution():
    # Define the number of hangers for each color
    pink_hangers = 7
    green_hangers = 4
    blue_hangers = green_hangers - 1
    yellow_hangers = blue_hangers - 1

    # Calculate the total number of hangers
    total_hangers = pink_hangers + green_hangers + blue_hangers + yellow_hangers
    result = total_hangers
    return result

print(solution())
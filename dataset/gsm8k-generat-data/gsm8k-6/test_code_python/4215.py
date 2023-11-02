def solution():
    # Calculate the total time John spends on drawing all the pictures
    drawing_time = 10 * 2  # it takes 2 hours to draw each picture

    # Calculate the time John spends on coloring all the pictures
    color_time = (0.7 * 2) * 10  # it takes 30% less time to color each picture

    # Calculate the total time John spends on all the pictures
    total_time = drawing_time + color_time
    result = total_time
    return result

print(solution())
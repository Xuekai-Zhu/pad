def solution():
    # Define the number of pictures and the time it takes to draw each picture
    num_pictures = 10
    draw_time = 2

    # Calculate the reduced coloring time
    reduced_color_time = 0.7 * draw_time

    # Calculate the total time spent on all the pictures
    total_time = num_pictures * (draw_time + reduced_color_time)
    result = total_time
    return result

print(solution())
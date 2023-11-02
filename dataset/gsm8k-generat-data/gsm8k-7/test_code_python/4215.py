def solution():
    num_pictures = 10
    draw_time_per_picture = 2 # in hours
    color_time_reduction = 0.3 # 30% reduction in time taken to color each picture

    # Calculate the total time John spends drawing all pictures
    total_draw_time = num_pictures * draw_time_per_picture

    # Calculate the total time John spends coloring all pictures
    color_time_per_picture = draw_time_per_picture * (1 - color_time_reduction)
    total_color_time = num_pictures * color_time_per_picture

    # Calculate the total time John spends on all pictures
    total_time = total_draw_time + total_color_time
    result = total_time
    return result

print(solution())
def solution():
    
    draw_time = 2
    color_time = 0.7 * draw_time
    total_time_per_picture = draw_time + color_time
    total_pictures = 10
    total_time = total_time_per_picture * total_pictures
    result = total_time
    return result

print(solution())
def solution():
    """John decides to take up illustration. He draws and colors 10 pictures. It takes him 2 hours to draw each picture and 30% less time to color each picture. How long does he spend on all the pictures?"""
    draw_time = 2
    color_time = 0.7 * draw_time
    total_time_per_picture = draw_time + color_time
    total_pictures = 10
    total_time = total_time_per_picture * total_pictures
    result = total_time
    return result

print(solution())
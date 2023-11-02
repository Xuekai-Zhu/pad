def solution():
    """John decides to take up illustration. He draws and colors 10 pictures. It takes him 2 hours to draw each picture and 30% less time to color each picture. How long does he spend on all the pictures?"""
    # Define the time it takes John to draw one picture and the percentage of time saved when coloring
    draw_time = 2
    color_time_saved_percent = 0.3

    # Calculate the time it takes John to color one picture
    color_time_saved = draw_time * color_time_saved_percent
    color_time = draw_time - color_time_saved

    # Calculate the total time it takes John to draw and color all the pictures
    total_time = (draw_time + color_time) * 10

    # Return the result
    result = total_time
    return result

print(solution())
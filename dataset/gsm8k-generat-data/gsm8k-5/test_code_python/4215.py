def solution():
    drawings = 10  # John draws and colors 10 pictures
    drawing_time = 2  # It takes John 2 hours to draw each picture
    coloring_time = drawing_time * 0.7  # John takes 30% less time to color each picture

    # Calculate the total time John spent on all the pictures
    total_time = (drawing_time + coloring_time) * drawings
    result = total_time
    return result

print(solution())
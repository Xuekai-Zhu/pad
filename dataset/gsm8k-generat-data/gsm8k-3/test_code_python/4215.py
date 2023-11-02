def solution():
    """John decides to take up illustration. He draws and colors 10 pictures. It takes him 2 hours to draw each picture and 30% less time to color each picture. How long does he spend on all the pictures?"""
    # Define the time it takes to draw and color one picture
    DRAW_TIME = 2
    COLOR_TIME = DRAW_TIME * 0.7

    # Define the number of pictures
    num_pictures = 10

    # Calculate the total time spent on all the pictures
    total_time = num_pictures * (DRAW_TIME + COLOR_TIME)

    # Display the total time spent
    result = total_time
    return result

print(solution())
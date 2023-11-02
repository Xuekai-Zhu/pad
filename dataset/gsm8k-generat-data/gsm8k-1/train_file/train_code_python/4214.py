def solution():
    """John decides to take up illustration. He draws and colors 10 pictures. It takes him 2 hours to draw each picture and 30% less time to color each picture. How long does he spend on all the pictures?"""
    pictures = 10
    drawing_time = 2
    coloring_time = drawing_time * 0.7
    total_time = (drawing_time + coloring_time) * pictures
    result = total_time
    return result

print(solution())
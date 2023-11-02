def solution():
    
    pictures = 10
    drawing_time = 2
    coloring_time = drawing_time * 0.7
    total_time = (drawing_time + coloring_time) * pictures
    result = total_time
    return result

print(solution())
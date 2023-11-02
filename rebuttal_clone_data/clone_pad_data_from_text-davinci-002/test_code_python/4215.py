def solution():
    num_pictures = 10
    time_drawing_per_picture = 2
    time_coloring_per_picture = time_drawing_per_picture * .7
    total_time = time_drawing_per_picture * num_pictures + time_coloring_per_picture * num_pictures
    result = total_time
    return result

print(solution())
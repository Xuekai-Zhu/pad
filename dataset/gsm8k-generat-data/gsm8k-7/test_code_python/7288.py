def solution():
    speed = 10      # miles per hour
    time_length = 2 # hours
    time_width = 0.5 # hours
    length = speed * time_length
    width = speed * time_width

    # Calculate the area of the lake in square miles
    area = length * width
    result = area
    return result

print(solution())
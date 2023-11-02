def solution():
    speed = 10  # The boat travels at a speed of 10 MPH
    time_length = 2  # It takes 2 hours to go across the length of the lake
    time_width = 0.5  # It takes 30 minutes to go across the width of the lake (0.5 hours)

    # Calculate the length of the lake
    length = speed * time_length

    # Calculate the width of the lake
    width = speed * time_width

    # Calculate the area of the lake
    area = length * width
    result = area
    return result

print(solution())
def solution():
    # Define Georgie's initial speed and distance
    initial_speed = 40 / 5 # yards per second
    initial_distance = initial_speed * 10 # yards in 10 seconds

    # Calculate Georgie's improved speed and distance
    improved_speed = initial_speed * 1.4
    improved_distance = improved_speed * 10

    result = improved_distance
    return result

print(solution())
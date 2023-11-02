def solution():
    initial_speed = 40 / 5  # Georgie can run 40 yards in 5 seconds
    improved_speed = initial_speed * 1.4  # Georgie can improve his speed by 40%
    time = 10  # Georgie wants to know how many yards he can run in 10 seconds

    # Calculate the distance Georgie can run in 10 seconds
    distance = improved_speed * time
    result = distance
    return result

print(solution())
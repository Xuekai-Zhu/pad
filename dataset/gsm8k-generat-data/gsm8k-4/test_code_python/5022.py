def solution():
    """Georgie is a varsity player on a football team. He can run 40 yards within 5 seconds. If he can improve his speed by forty percent, how many yards will he be able to run within 10 seconds?"""
    # Define the initial speed and distance
    initial_speed = 40 / 5  # 8 yards per second
    initial_distance = initial_speed * 10  # 80 yards in 10 seconds

    # Calculate the improved speed and distance
    improved_speed = initial_speed * 1.4  # 40% faster
    improved_distance = improved_speed * 10  # 140% farther

    # Return the result
    result = improved_distance
    return result

print(solution())
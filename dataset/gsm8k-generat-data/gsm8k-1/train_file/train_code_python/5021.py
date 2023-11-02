def solution():
    """Georgie is a varsity player on a football team. He can run 40 yards within 5 seconds. If he can improve his speed by forty percent, how many yards will he be able to run within 10 seconds?"""
    initial_speed = 40/5 # in yards per second
    improved_speed = initial_speed * 1.4
    time = 10 # in seconds
    distance = improved_speed * time
    result = distance
    return result

print(solution())
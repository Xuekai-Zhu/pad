def solution():
    """Georgie is a varsity player on a football team. He can run 40 yards within 5 seconds. If he can improve his speed by forty percent, how many yards will he be able to run within 10 seconds?"""
    original_speed = 40 / 5  # yards per second
    improved_speed = original_speed * 1.4  # yards per second
    yards_in_10_sec = improved_speed * 10
    result = yards_in_10_sec
    return result

print(solution())
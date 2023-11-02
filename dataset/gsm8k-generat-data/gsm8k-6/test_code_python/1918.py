def solution():
    # Calculate the height of the ball after each bounce
    height = 96  # height of the building
    for i in range(5):
        height = height / 2  # ball bounces to half the height from which it fell on each bounce
    
    result = height
    return result

print(solution())
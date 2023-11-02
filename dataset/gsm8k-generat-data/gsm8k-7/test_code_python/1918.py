def solution():
    height = 96

    # Calculate the height of the ball after each bounce
    for i in range(5):
        height = height * 0.5

    result = height
    return result

print(solution())
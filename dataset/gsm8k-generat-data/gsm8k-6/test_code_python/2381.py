def solution():
    # Calculate the total number of balls in the box
    total_balls = 6 + 4 + 3*6 + 2*4  # the box contains 6 blue balls, 4 red balls, 3 times as many green balls as blue ones and twice as many yellow ones as red ones
    result = total_balls
    return result

print(solution())
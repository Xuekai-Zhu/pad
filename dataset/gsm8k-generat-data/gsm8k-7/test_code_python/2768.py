def solution():
    robert_balls = 25
    tim_balls = 40

    # Calculate how many balls Tim gave to Robert
    tim_gave = tim_balls / 2

    # Add Tim's balls to Robert's balls
    total_balls = robert_balls + tim_gave
    result = total_balls
    return result

print(solution())
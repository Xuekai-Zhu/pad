def solution():
    initial_height = 96  # The ball is dropped from a 96-foot tall building
    bounce_height_ratio = 0.5  # The ball bounces to half the height from which it fell on each bounce
    bounces = 5  # We want to know the height of the ball after the fifth bounce

    # Calculate the height of the ball after each bounce
    height_after_bounce = initial_height
    for i in range(bounces):
        height_after_bounce = height_after_bounce * bounce_height_ratio

    result = height_after_bounce
    return result

print(solution())
def solution():
    """Tim drops a ball off the roof of a 96-foot tall building. The ball bounces to half the height from which it fell on each bounce. How high will it bounce on the fifth bounce?"""
    # Define the initial height and number of bounces
    initial_height = 96
    num_bounces = 5

    # Calculate the height of the ball on each bounce
    bounce_height = initial_height
    for i in range(num_bounces):
        bounce_height /= 2

    # Display the height of the ball on the fifth bounce
    result = bounce_height
    return result

print(solution())
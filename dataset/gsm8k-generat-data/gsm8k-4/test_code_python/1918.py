def solution():
    """Tim drops a ball off the roof of a 96-foot tall building. The ball bounces to half the height from which it fell on each bounce. How high will it bounce on the fifth bounce?"""
    # Define the initial height and number of bounces
    initial_height = 96
    num_bounces = 5

    # Calculate the height after each bounce
    height = initial_height  # The first bounce is from the roof
    for i in range(num_bounces):
        height /= 2  # The ball bounces to half the height of the previous bounce

    # Display the height after the final bounce
    result = height
    return result

print(solution())
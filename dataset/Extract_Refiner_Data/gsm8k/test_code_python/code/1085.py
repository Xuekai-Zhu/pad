def solution():
    
    # Define the initial height of the ball and the height ratio between the ball and the first bounce
    initial_height = 24 * 3
    height_ratio = 2/3

    # Calculate the height of the ball on the second bounce
    second_bounce_height = initial_height * height_ratio * 2

    # Display the height of the ball on the second bounce
    result = second_bounce_height
    return result

print(solution())
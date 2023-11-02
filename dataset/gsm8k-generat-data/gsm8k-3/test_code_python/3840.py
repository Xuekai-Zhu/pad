def solution():
    """Fred has 38 red marbles, half as many green ones, and the rest are dark blue. If he has 63 marbles, how many of them are dark blue?"""
    # Calculate the number of green marbles
    green_marbles = 38/2

    # Calculate the total number of red and green marbles
    total_red_green = 38 + green_marbles

    # Calculate the number of dark blue marbles
    dark_blue = 63 - total_red_green

    # Display the number of dark blue marbles
    result = dark_blue
    return result

print(solution())
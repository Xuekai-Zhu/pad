def solution():
    # Calculate the number of green marbles Fred has
    green_marbles = 38 / 2

    # Calculate the number of dark blue marbles Fred has
    dark_blue_marbles = 63 - 38 - green_marbles

    result = dark_blue_marbles
    return result

print(solution())
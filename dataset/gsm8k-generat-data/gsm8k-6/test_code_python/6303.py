def solution():
    # Calculate the number of dark blue marbles
    dark_blue = 63 / 3  

    # Calculate the total number of non-green marbles
    non_green = 63 - 4  

    # Calculate the number of red marbles
    red = non_green - dark_blue  

    result = red
    return result

print(solution())
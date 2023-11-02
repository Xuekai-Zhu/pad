def solution():
    # Calculate the original number of red and blue marbles
    original_red_blue = (50 - 20) / 2  
    original_white = 20

    # Calculate the number of marbles removed by Jack
    removed_marbles = 2 * (original_white - original_red_blue)

    # Calculate the number of marbles left in the box
    remaining_marbles = 50 - removed_marbles
    result = remaining_marbles
    return result

print(solution())
def solution():
    num_white_cookies = 80
    num_black_cookies = num_white_cookies + 50

    # Calculate how many black cookies Cristian will have left after eating half
    num_black_remaining = num_black_cookies / 2

    # Calculate how many white cookies Cristian will have left after eating 3/4
    num_white_remaining = num_white_cookies / 4

    # Calculate the total number of cookies remaining in the jar
    total_remaining = num_black_remaining + num_white_remaining
    result = total_remaining
    return result

print(solution())
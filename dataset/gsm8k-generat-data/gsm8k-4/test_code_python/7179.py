def solution():
    """Three baskets A, B and C contain different numbers of differently colored marbles. Basket A contains 4 red marbles and 2 yellow marbles. Basket B contains 6 green marbles and 1 yellow marble. Basket C contains 3 white marbles and 9 yellow marbles. What is the difference between the number of each color of marble in the basket that has the greatest difference?"""
    # Define the numbers of marbles in each basket
    a_red = 4
    a_yellow = 2
    b_green = 6
    b_yellow = 1
    c_white = 3
    c_yellow = 9

    # Calculate the differences between the colors in each basket
    a_diff = abs(a_red - a_yellow)
    b_diff = abs(b_green - b_yellow)
    c_diff = abs(c_white - c_yellow)

    # Determine the basket with the greatest difference
    greatest_diff = max(a_diff, b_diff, c_diff)

    # Calculate the difference between the colors in the basket with the greatest difference
    if greatest_diff == a_diff:
        color_diff = abs(a_red - a_yellow)
    elif greatest_diff == b_diff:
        color_diff = abs(b_green - b_yellow)
    else:
        color_diff = abs(c_white - c_yellow)

    # Return the result
    result = color_diff
    return result

print(solution())
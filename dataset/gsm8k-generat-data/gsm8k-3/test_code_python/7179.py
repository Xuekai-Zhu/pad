def solution():
    """Three baskets A, B and C contain different numbers of differently colored marbles. Basket A contains 4 red marbles and 2 yellow marbles. Basket B contains 6 green marbles and 1 yellow marble. Basket C contains 3 white marbles and 9 yellow marbles. What is the difference between the number of each color of marble in the basket that has the greatest difference?"""
    # Define the number of marbles in each basket
    A_red = 4
    A_yellow = 2
    B_green = 6
    B_yellow = 1
    C_white = 3
    C_yellow = 9

    # Calculate the difference in the number of red marbles between baskets
    red_diff = abs(A_red - B_green)
    if abs(B_green - C_white) > red_diff:
        red_diff = abs(B_green - C_white)
    if abs(C_white - A_red) > red_diff:
        red_diff = abs(C_white - A_red)

    # Calculate the difference in the number of yellow marbles between baskets
    yellow_diff = abs(A_yellow - B_yellow)
    if abs(B_yellow - C_yellow) > yellow_diff:
        yellow_diff = abs(B_yellow - C_yellow)
    if abs(C_yellow - A_yellow) > yellow_diff:
        yellow_diff = abs(C_yellow - A_yellow)

    # Display the greatest difference
    greatest_diff = max(red_diff, yellow_diff)
    result = greatest_diff
    return result

print(solution())
def solution():
    # Calculate the total number of marbles of each color in each basket
    basket_A_red = 4
    basket_A_yellow = 2
    basket_B_green = 6
    basket_B_yellow = 1
    basket_C_white = 3
    basket_C_yellow = 9

    # Calculate the difference between the number of each color of marble in each basket
    diff_A = abs(basket_A_red - basket_A_yellow)
    diff_B = abs(basket_B_green - basket_B_yellow)
    diff_C = abs(basket_C_white - basket_C_yellow)

    # Find the basket with the greatest difference and calculate the difference between the number of each color of marble in that basket
    greatest_diff = max(diff_A, diff_B, diff_C)
    if greatest_diff == diff_A:
        result = abs(basket_A_red - basket_A_yellow)
    elif greatest_diff == diff_B:
        result = abs(basket_B_green - basket_B_yellow)
    else:
        result = abs(basket_C_white - basket_C_yellow)

    return result

print(solution())
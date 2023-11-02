def solution():
    # Calculate the total square footage of the first 3 paintings
    square_ft_3 = 3 * 5 * 5  # 3 paintings are 5ft by 5ft

    # Calculate the square footage of the fourth painting
    square_ft_4 = 10 * 8  # 1 painting is 10ft by 8ft

    # Calculate the total square footage of the 4 paintings
    total_square_ft = square_ft_3 + square_ft_4

    # Calculate the square footage of the fifth painting
    square_ft_5 = 200 - total_square_ft

    # Calculate the width of the fifth painting
    width_5 = square_ft_5 / 5  # the height is 5ft

    result = width_5
    return result

print(solution())
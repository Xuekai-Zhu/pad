def solution():
    # Calculate the sum of Yuri's dice
    yuri_sum = 2 + 4 + 5

    # Calculate the minimum and maximum possible value of Yuko's last die
    min_value = yuri_sum - 5 - 1  # the lowest possible sum for Yuko is Yuri's sum minus 5 (the maximum value of the other two dice) minus 1 (the minimum value for Yuko's first die)
    max_value = yuri_sum - 5  # the highest possible sum for Yuko is Yuri's sum minus 5 (the maximum value of the other two dice)

    # Calculate the number of squares that Yuko's last die must move him to be in front of his brother
    result = max_value - 6  # Yuko needs to move at least 1 square ahead of his brother, and each value above 6 moves him one square ahead
    return result

print(solution())
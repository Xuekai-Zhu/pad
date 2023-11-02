def solution():
    num_red_balloons = 20
    num_green_balloons = 15

    # Subtract the number of burst balloons from the total number of balloons
    num_red_balloons_left = num_red_balloons - 3
    num_green_balloons_left = num_green_balloons - 2

    # Calculate the total number of balloons left
    total_balloons_left = num_red_balloons_left + num_green_balloons_left
    result = total_balloons_left
    return result

print(solution())
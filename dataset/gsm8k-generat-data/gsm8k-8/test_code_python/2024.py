def solution():
    # Define the initial number of red and green balloons
    red_balloons = 20
    green_balloons = 15

    # Subtract the number of burst balloons from each color
    red_balloons -= 3
    green_balloons -= 2

    # Calculate the total number of balloons left
    total_balloons = red_balloons + green_balloons
    result = total_balloons
    return result

print(solution())
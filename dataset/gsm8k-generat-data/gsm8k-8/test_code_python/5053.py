def solution():
    # Define variables for the time and number of colors
    total_time = 120
    color_change_time = 10
    number_of_colors = 0

    # Loop through each 10-minute interval during the sunset
    for time in range(0, total_time, color_change_time):
        number_of_colors += 1

    # Return the total number of colors the sky turned
    result = number_of_colors
    return result

print(solution())
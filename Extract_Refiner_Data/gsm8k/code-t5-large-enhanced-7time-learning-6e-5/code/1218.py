def solution():
    
    # Define the width of each window in inches
    WINDOW_WIDTH = 35

    # Define the number of windows
    num_windows = 5

    # Calculate the total width of the windows
    total_width = WINDOW_WIDTH * num_windows

    # Calculate the amount of fabric Luke needs to buy
    fabric_width = total_width * 2

    # Display the amount of fabric Luke needs to buy
    result = fabric_width
    return result

print(solution())
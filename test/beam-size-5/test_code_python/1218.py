def solution():
    
    # Define the width of each window and the number of windows
    WINDOWS_WIDTH = 35
    WINDOWS_COUNT = 5

    # Calculate the total width of the windows
    total_width = WINDOWS_WIDTH * WINDOWS_COUNT

    # Calculate the number of fabric Luke needs to buy
    fabric_needed = 2 * total_width

    # Display the number of fabric Luke needs to buy
    result = fabric_needed
    return result

print(solution())
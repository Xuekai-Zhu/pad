def solution():
    
    # Define the dimensions of each box and the walls
    LENGTH = 5
    WIDTH = 6
    HEIGHT = 4
    WALL_LENGTH = 1
    WALL_WIDTH = 1

    # Calculate the volume of each box
    box_volume = LENGTH * WIDTH * HEIGHT

    # Calculate the total volume of all 3 boxes
    total_volume = box_volume * 3

    # Calculate the total volume of all 3 boxes with the walls
    total_volume += WALL_LENGTH * WALL_WIDTH

    # Display the total volume
    result = total_volume
    return result

print(solution())
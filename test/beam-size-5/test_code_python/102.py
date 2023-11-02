def solution():
    
    # Define the dimensions of each box
    LENGTH = 5
    WIDTH = 6
    HEIGHT = 4

    # Calculate the volume of each box
    box_volume = LENGTH * WIDTH * HEIGHT

    # Calculate the total volume of all 3 boxes
    total_volume = box_volume * 3

    # Display the total volume
    result = total_volume
    return result

print(solution())
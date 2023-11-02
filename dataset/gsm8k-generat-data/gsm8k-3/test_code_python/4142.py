def solution():
    """Quinten sees three buildings downtown and decides to estimate their heights. He knows from a book on local buildings that the one in the middle is 100 feet tall. The one on the left looks like it is 80% of the height of the middle one. The one on the right looks 20 feet shorter than if the building on the left and middle were stacked on top of each other. How tall does Quinten estimate their total height to be?"""
    
    # Define the height of the middle building as a constant
    HEIGHT_MIDDLE = 100
    
    # Calculate the height of the left building
    HEIGHT_LEFT = 0.8 * HEIGHT_MIDDLE
    
    # Calculate the height of the stacked left and middle buildings
    stacked_height = HEIGHT_LEFT + HEIGHT_MIDDLE
    
    # Calculate the height of the right building
    HEIGHT_RIGHT = stacked_height - 20
    
    # Calculate the total height
    total_height = HEIGHT_LEFT + HEIGHT_MIDDLE + HEIGHT_RIGHT
    
    # Display the estimated total height
    result = total_height
    return result

print(solution())
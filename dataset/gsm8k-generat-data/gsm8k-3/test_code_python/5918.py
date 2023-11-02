def solution():
    """Jo-Bob hopped into the hot air balloon, released the anchor rope, and pulled on the lift chain, which ignited the flame and provided the warm air that caused the balloon to rise.  When the lift chain was pulled, the balloon would rise at a rate of 50 feet per minute.  But when the chain was not being pulled, the balloon would slowly descend at a rate of 10 feet per minute.  During his balloon ride, he pulled the chain for 15 minutes, then released the rope for 10 minutes, then pulled the chain for another 15 minutes, and finally released the chain and allowed the balloon to slowly descend back to the earth.  During his balloon ride, what was the highest elevation reached by the balloon?"""
    # Define the rates of ascent and descent
    ASCENT_RATE = 50
    DESCENT_RATE = 10

    # Initialize the highest elevation and current elevation
    highest_elevation = 0
    current_elevation = 0

    # First ascent
    current_elevation += ASCENT_RATE * 15
    if current_elevation > highest_elevation:
        highest_elevation = current_elevation

    # Descent
    current_elevation -= DESCENT_RATE * 10

    # Second ascent
    current_elevation += ASCENT_RATE * 15
    if current_elevation > highest_elevation:
        highest_elevation = current_elevation

    # Descent to earth
    while current_elevation > 0:
        current_elevation -= DESCENT_RATE

    # Display the highest elevation reached
    result = highest_elevation
    return result

print(solution())
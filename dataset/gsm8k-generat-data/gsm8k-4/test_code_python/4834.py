def solution():
    """James wants to build a ladder to climb a very tall tree. Each rung of the ladder is 18 inches long and they are 6 inches apart. If he needs to climb 50 feet how many feet of wood will he need for the rungs?"""
    # Define the length of each rung and the distance between them in inches
    RUNG_LENGTH = 18
    RUNG_GAP = 6
    
    # Define the total distance James needs to climb in feet
    TOTAL_CLIMB_DISTANCE = 50
    
    # Calculate the total number of rungs needed
    total_rungs = (TOTAL_CLIMB_DISTANCE * 12) / RUNG_GAP
    
    # Calculate the total length of wood needed for the rungs
    total_wood_length = total_rungs * RUNG_LENGTH / 12
    
    # Return the result in feet
    result = total_wood_length
    return result

print(solution())
def solution():
    """There are 18 green leaves on each of the 3 tea leaf plants. One-third of them turn yellow and fall off on each of the tea leaf plants.  How many green leaves are left on the tea leaf plants?"""
    
    # Define the number of green leaves per tea leaf plant and the fraction that turn yellow and fall off
    GREEN_LEAVES = 18
    YELLOW_LEAVES_FRACTION = 1/3
    
    # Calculate the number of yellow leaves that fall off each tea leaf plant
    yellow_leaves_per_plant = GREEN_LEAVES * YELLOW_LEAVES_FRACTION
    
    # Calculate the number of green leaves remaining on each tea leaf plant
    green_leaves_per_plant = GREEN_LEAVES - yellow_leaves_per_plant
    
    # Calculate the total number of green leaves remaining on all three tea leaf plants
    total_green_leaves = green_leaves_per_plant * 3
    
    # Display the total number of green leaves remaining on the tea leaf plants
    result = total_green_leaves
    return result

print(solution())
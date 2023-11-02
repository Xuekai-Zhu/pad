def solution():
    """In mid-May, the depth of a river in Moreland is measured. By mid-June, the river is 10 feet deeper than mid-May. By mid-July, the river is three times deeper than mid-June. If the river is 45 feet deep in mid-July, how many feet deep was the river in mid-May?"""
    
    # Define the depth of the river in mid-May
    depth_may = None
    
    # Calculate the depth of the river in mid-June
    depth_june = depth_may + 10
    
    # Calculate the depth of the river in mid-July
    depth_july = depth_june * 3
    
    # Solve for the depth of the river in mid-May
    depth_may = (depth_july/3) - 10
    
    result = depth_may
    return result

print(solution())
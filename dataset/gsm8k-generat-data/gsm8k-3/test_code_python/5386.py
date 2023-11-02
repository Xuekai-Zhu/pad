def solution():
    """Erin counts six trolls hiding by the path, 6 less than four times that number of trolls hiding under the bridge,
    and half as many trolls hiding in the plains as under the bridge. How many trolls did she count in total?"""
    
    # Define the number of trolls by the path
    trolls_path = 6
    
    # Calculate the number of trolls under the bridge
    trolls_bridge = 4 * trolls_path - 6
    
    # Calculate the number of trolls in the plains
    trolls_plains = trolls_bridge / 2
    
    # Calculate the total number of trolls counted
    total_trolls = trolls_path + trolls_bridge + trolls_plains
    
    # Display the total number of trolls counted
    result = total_trolls
    return result

print(solution())
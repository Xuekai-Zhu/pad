def solution():
    """Kimberley, Ela, and Houston all are sent to collect firewood by their grammy. Kimberley collects ten pounds of firewood, and Houston collects 12 pounds of firewood. If the three of them managed to collect a total of 35 pounds of firewood, how many pounds were collected by Ela?"""
    
    # Calculate the total firewood collected by Kimberley and Houston
    total_collected = 10 + 12
    
    # Calculate the firewood collected by Ela
    ela_collected = 35 - total_collected
    
    result = ela_collected
    return result

print(solution())
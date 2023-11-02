def solution():
    """In ancient China, soldiers positioned in beacon towers along the Great Wall would send smoke signals to warn of impending attacks.  Since the towers were located at 5 kilometer intervals, they could send a signal the length of the Great Wall.  If the Great wall was 7300 kilometers long, and every tower had two soldiers, what was the combined number of soldiers in beacon towers on the Great Wall?"""
    # Calculate the number of towers along the Great Wall
    num_towers = 7300 // 5

    # Calculate the total number of soldiers in the towers
    num_soldiers = num_towers * 2

    # Display the combined number of soldiers in beacon towers on the Great Wall
    result = num_soldiers
    return result

print(solution())
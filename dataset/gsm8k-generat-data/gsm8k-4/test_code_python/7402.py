def solution():
    """In ancient China, soldiers positioned in beacon towers along the Great Wall would send smoke signals to warn of impending attacks. Since the towers were located at 5 kilometer intervals, they could send a signal the length of the Great Wall. If the Great wall was 7300 kilometers long, and every tower had two soldiers, what was the combined number of soldiers in beacon towers on the Great Wall?"""
    # Define the distance between two towers and the length of the Great Wall
    distance_between_towers = 5
    great_wall_length = 7300

    # Calculate the number of towers
    number_of_towers = great_wall_length / distance_between_towers

    # Calculate the number of soldiers
    number_of_soldiers = number_of_towers * 2

    result = number_of_soldiers
    return result

print(solution())
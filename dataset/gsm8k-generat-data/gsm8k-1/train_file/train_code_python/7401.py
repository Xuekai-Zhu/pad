def solution():
    """In ancient China, soldiers positioned in beacon towers along the Great Wall would send smoke signals to warn of impending attacks. Since the towers were located at 5 kilometer intervals, they could send a signal the length of the Great Wall. If the Great wall was 7300 kilometers long, and every tower had two soldiers, what was the combined number of soldiers in beacon towers on the Great Wall?"""
    tower_distance = 5
    great_wall_length = 7300
    number_of_towers = great_wall_length // tower_distance
    soldiers_per_tower = 2
    total_soldiers = number_of_towers * soldiers_per_tower
    result = total_soldiers
    return result

print(solution())
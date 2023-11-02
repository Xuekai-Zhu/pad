def solution():
    # Calculate the total number of towers along the Great Wall
    num_towers = 7300 / 5  # the towers were located at 5 kilometer intervals

    # Calculate the total number of soldiers in beacon towers
    num_soldiers = num_towers * 2  # every tower had two soldiers

    result = num_soldiers
    return result

print(solution())
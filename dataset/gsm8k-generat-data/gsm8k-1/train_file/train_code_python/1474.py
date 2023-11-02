def solution():
    """Pete has a bag with 10 marbles. 40% are blue and the rest are red. His friend will trade him two blue marbles for every red one. If Pete keeps 1 red marble, how many total marbles does he have after trading with his friend?"""
    total_marbles = 10
    blue_marbles = total_marbles * 0.4
    red_marbles = total_marbles - blue_marbles
    
    # Pete trades all but one red marble for blue marbles
    red_marbles_traded = red_marbles - 1
    blue_marbles_received = red_marbles_traded * 2
    
    # Pete keeps one red marble and adds the received blue marbles
    total_marbles = 1 + blue_marbles_received
    
    result = total_marbles
    return result

print(solution())
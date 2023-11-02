def solution():
    
    total_marbles = 28
    num_bags = 4
    marbles_per_bag = total_marbles / num_bags
    marbles_left = total_marbles - marbles_per_bag
    result = marbles_left
    return result

print(solution())
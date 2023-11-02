def solution():

    original_green_marbles = 26
    num_bags_of_blue_marbles = 6
    num_marbles_ Per_bag = 10
    total_blue_marbles = num_bags_of_blue_marbles * num_marbles_per_bag
    marbles_given_away = 6 + 8
    
    result = original_green_marbles + total_blue_marbles - marbles_given_away

    return result

print(solution())
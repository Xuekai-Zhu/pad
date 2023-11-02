def solution():
    jack_weight = 60
    anna_weight = 40
    rock_weight = 4
    
    # Calculate the difference in weight between Jack and Anna
    weight_diff = jack_weight - anna_weight
    
    # Calculate the number of rocks needed to balance their weights
    num_rocks = weight_diff / rock_weight
    
    result = num_rocks
    return result

print(solution())
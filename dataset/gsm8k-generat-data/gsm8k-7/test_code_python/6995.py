def solution():
    total_animals = 70
    ratio_of_rats_to_chihuahuas = 6
    
    # Calculate the number of chihuahuas
    num_chihuahuas = total_animals / (1 + ratio_of_rats_to_chihuahuas)
    
    # Calculate the number of rats
    num_rats = ratio_of_rats_to_chihuahuas * num_chihuahuas
    result = num_rats
    return result

print(solution())
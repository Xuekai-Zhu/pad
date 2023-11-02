def solution():
    
    num_pregnant_dogs = 3
    puppies_per_dog = 4
    num_puppies = num_pregnant_dogs * puppies_per_dog
    num_shots_per_puppy = 2
    cost_per_shot = 5
    total_cost = num_puppies * num_shots_per_puppy * cost_per_shot
    result = total_cost
    return result

print(solution())
def solution():
    num_pregnant_dogs = 3
    puppies_per_dog = 4
    shots_per_puppy = 2
    cost_per_shot = 5

    # Calculate the total number of puppies
    total_puppies = num_pregnant_dogs * puppies_per_dog

    # Calculate the total number of shots needed
    total_shots = total_puppies * shots_per_puppy

    # Calculate the total cost of all shots
    total_cost = total_shots * cost_per_shot
    result = total_cost
    return result

print(solution())
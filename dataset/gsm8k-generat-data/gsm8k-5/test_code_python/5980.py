def solution():
    num_dogs = 3  # Chuck has 3 pregnant dogs
    puppies_per_dog = 4  # Each dog gives birth to 4 puppies
    shots_per_puppy = 2  # Each puppy needs 2 shots
    cost_per_shot = 5  # Each shot costs $5

    # Calculate the total number of puppies
    total_puppies = num_dogs * puppies_per_dog

    # Calculate the total number of shots
    total_shots = total_puppies * shots_per_puppy

    # Calculate the total cost of the shots
    total_cost = total_shots * cost_per_shot
    result = total_cost
    return result

print(solution())
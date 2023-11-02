def solution():
    """Chuck breeds dogs. He has 3 pregnant dogs. They each give birth to 4 puppies. Each puppy needs 2 shots and each shot costs $5. How much did the shots cost?"""
    num_pregnant_dogs = 3
    num_puppies_per_dog = 4
    num_puppies_total = num_pregnant_dogs * num_puppies_per_dog
    num_shots_per_puppy = 2
    cost_per_shot = 5
    total_cost = num_puppies_total * num_shots_per_puppy * cost_per_shot
    result = total_cost
    return result

print(solution())
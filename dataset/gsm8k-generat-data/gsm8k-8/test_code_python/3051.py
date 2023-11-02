def solution():
    # Define the costs for each type of animal
    cat_cost = 50
    adult_dog_cost = 100
    puppy_cost = 150

    # Determine the number of animals adopted
    num_cats = 2
    num_adult_dogs = 3
    num_puppies = 2

    # Calculate the total cost to get the animals ready for adoption
    total_cost = (num_cats * cat_cost) + (num_adult_dogs * adult_dog_cost) + (num_puppies * puppy_cost)
    result = total_cost
    return result

print(solution())
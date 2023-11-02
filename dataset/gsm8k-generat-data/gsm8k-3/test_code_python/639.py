def solution():
    """In a community of 50 families, 15 families own 2 dogs, 20 families own 1 dog, while the remaining families own 2 cats each. How many dogs and cats are there in all?"""
    # Define the number of families and the number of dogs/cats each family owns
    num_families = 50
    num_dogs_2 = 15 * 2
    num_dogs_1 = 20
    num_cats_2 = (num_families - 15 - 20) * 2

    # Calculate the total number of dogs and cats
    total_dogs = num_dogs_2 + num_dogs_1
    total_cats = num_cats_2

    # Display the total number of dogs and cats
    result = f"There are {total_dogs} dogs and {total_cats} cats in the community."
    return result

print(solution())
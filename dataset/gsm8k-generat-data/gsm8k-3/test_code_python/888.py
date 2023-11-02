def solution():
    """Teddy has 7 dogs and 8 cats. Ben has 9 more dogs than Teddy, and Dave has 13 more cats and 5 less dogs than Teddy. How many pets do all of them have combined?"""
    # Define the number of dogs and cats each person has
    teddy_dogs = 7
    teddy_cats = 8
    ben_dogs = teddy_dogs + 9
    ben_cats = teddy_cats
    dave_dogs = teddy_dogs - 5
    dave_cats = teddy_cats + 13

    # Calculate the total number of pets
    total_dogs = teddy_dogs + ben_dogs + dave_dogs
    total_cats = teddy_cats + ben_cats + dave_cats
    total_pets = total_dogs + total_cats

    # Display the total number of pets
    result = total_pets
    return result

print(solution())
def solution():
    """Teddy has 7 dogs and 8 cats. Ben has 9 more dogs than Teddy, and Dave has 13 more cats and 5 less dogs than Teddy. How many pets do all of them have combined?"""
    # Define the number of dogs and cats for Teddy
    teddy_dogs = 7
    teddy_cats = 8

    # Define the number of dogs for Ben
    ben_dogs = teddy_dogs + 9

    # Define the number of cats for Dave
    dave_cats = teddy_cats + 13

    # Define the number of dogs for Dave
    dave_dogs = teddy_dogs - 5

    # Calculate the total number of dogs and cats
    total_dogs = teddy_dogs + ben_dogs + dave_dogs
    total_cats = teddy_cats + dave_cats

    # Calculate the total number of pets
    total_pets = total_dogs + total_cats

    # return the result
    result = total_pets
    return result

print(solution())
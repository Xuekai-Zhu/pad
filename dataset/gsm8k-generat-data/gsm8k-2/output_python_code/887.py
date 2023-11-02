def solution():
    """Teddy has 7 dogs and 8 cats. Ben has 9 more dogs than Teddy, and Dave has 13 more cats and 5 less dogs than Teddy. How many pets to they have combined?"""
    teddy_dogs = 7
    teddy_cats = 8
    ben_dogs = teddy_dogs + 9
    dave_cats = teddy_cats + 13
    dave_dogs = teddy_dogs - 5
    total_pets = teddy_dogs + teddy_cats + ben_dogs + dave_cats + dave_dogs
    result = total_pets
    return result

print(solution())
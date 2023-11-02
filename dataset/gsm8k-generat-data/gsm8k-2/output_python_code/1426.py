def solution():
    """The total number of dogs at an animal rescue center is 200. Mr. Tanner, the manager at the rescue center, gets a call that 100 dogs at another rescue center are to be moved because of weather problems. He agrees to bring the dogs to his rescue center, and after one week, gives out 40 animals for adoption. After a month, 60 more dogs were adopted by dog lovers. What's the total number of remaining animals in the adoption center after the last adoptions?"""
    initial_dogs = 200
    moved_dogs = 100
    remaining_dogs = initial_dogs + moved_dogs
    dogs_for_adoption = 40
    remaining_dogs -= dogs_for_adoption
    adoptions = 60
    remaining_dogs -= adoptions
    result = remaining_dogs
    return result

print(solution())
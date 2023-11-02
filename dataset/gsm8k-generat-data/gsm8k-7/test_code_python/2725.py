def solution():
    num_dogs = 40
    female_percentage = 0.6
    birth_rate = 3/4
    pups_per_female = 10
    donated_pups = 130

    # Calculate the number of female dogs
    num_female_dogs = num_dogs * female_percentage

    # Calculate the number of female dogs that gave birth
    num_mother_dogs = num_female_dogs * birth_rate

    # Calculate the total number of puppies
    total_pups = num_mother_dogs * pups_per_female

    # Calculate the number of puppies Tenisha has left after donation
    remaining_pups = total_pups - donated_pups
    result = remaining_pups
    return result

print(solution())
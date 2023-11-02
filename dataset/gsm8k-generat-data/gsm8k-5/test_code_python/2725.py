def solution():
    # Calculate the number of female dogs
    female_dogs = 0.6 * 40

    # Calculate the number of female dogs that give birth to 10 puppies each
    female_dogs_giving_birth = 0.75 * female_dogs

    # Calculate the total number of puppies
    total_puppies = 10 * female_dogs_giving_birth

    # Calculate the number of puppies donated to the church
    donated_puppies = 130

    # Calculate the number of puppies remaining with Tenisha
    remaining_puppies = total_puppies - donated_puppies
    result = remaining_puppies
    return result

print(solution())
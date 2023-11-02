def solution():
    # Calculate the number of female dogs
    female_dogs = 0.6 * 40

    # Calculate the number of female dogs that give birth to puppies
    female_dogs_with_puppies = 0.75 * female_dogs

    # Calculate the total number of puppies born
    total_puppies = 10 * female_dogs_with_puppies

    # Calculate the number of puppies remaining after donating to the church
    remaining_puppies = total_puppies - 130

    result = remaining_puppies
    return result

print(solution())
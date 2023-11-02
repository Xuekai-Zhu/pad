def solution():
    """Tenisha had 40 dogs that she kept at home as pets. If 60% of them are female, and 3/4 of the female gives birth to 10 puppies each, calculate the total number of puppies that Tenisha remains with after donating 130 puppies to the church."""
    # Define the initial number of dogs
    initial_dogs = 40

    # Calculate the number of female dogs
    female_dogs = 0.6 * initial_dogs

    # Calculate the number of female dogs that give birth to puppies
    female_birth = 0.75 * female_dogs

    # Calculate the total number of puppies
    puppies = female_birth * 10

    # Calculate the number of puppies remaining after donating to the church
    remaining_puppies = puppies - 130

    result = remaining_puppies
    return result

print(solution())
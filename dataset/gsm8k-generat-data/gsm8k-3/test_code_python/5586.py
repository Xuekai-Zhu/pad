def solution():
    """There are 400 students in a local high school. 50 percent are freshmen or sophomores.  1/5 of freshmen and sophomores own a pet.  How many freshmen and sophomores do not own a pet?"""
    # Calculate the total number of freshmen and sophomores
    freshmen_and_sophomores = 0.5 * 400

    # Calculate the number of freshmen and sophomores who own a pet
    pet_owners = 0.2 * freshmen_and_sophomores

    # Calculate the number of freshmen and sophomores who do not own a pet
    non_pet_owners = freshmen_and_sophomores - pet_owners

    # Display the number of freshmen and sophomores who do not own a pet
    result = non_pet_owners
    return result

print(solution())
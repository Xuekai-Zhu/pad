def solution():
    # Calculate the number of freshmen and sophomores
    freshmen_sophomores = 0.5 * 400

    # Calculate the number of freshmen and sophomores who own a pet
    pet_owners = (1/5) * freshmen_sophomores

    # Calculate the number of freshmen and sophomores who do not own a pet
    non_pet_owners = freshmen_sophomores - pet_owners
    result = non_pet_owners
    return result

print(solution())
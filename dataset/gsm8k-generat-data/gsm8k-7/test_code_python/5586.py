def solution():
    total_students = 400
    percent_fresh_soph = 0.5
    pet_owners_fresh_soph = 1/5

    # Calculate the number of freshmen and sophomores
    num_fresh_soph = total_students * percent_fresh_soph

    # Calculate the number of freshmen and sophomores who own a pet
    num_pet_owners = num_fresh_soph * pet_owners_fresh_soph

    # Calculate the number of freshmen and sophomores who do not own a pet
    num_no_pet = num_fresh_soph - num_pet_owners
    result = num_no_pet
    return result

print(solution())
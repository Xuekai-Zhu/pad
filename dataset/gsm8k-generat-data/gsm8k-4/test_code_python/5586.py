def solution():
    """There are 400 students in a local high school. 50 percent are freshmen or sophomores. 1/5 of freshmen and sophomores own a pet. How many freshmen and sophomores do not own a pet?"""
    # Define the total number of students and the percentage of freshmen and sophomores
    total_students = 400
    freshman_sophomore_percentage = 0.5

    # Calculate the number of freshmen and sophomores
    freshman_sophomore_count = total_students * freshman_sophomore_percentage

    # Calculate the number of freshmen and sophomores who own a pet
    pet_owners = freshman_sophomore_count * (1/5)

    # Calculate the number of freshmen and sophomores who do not own a pet
    non_pet_owners = freshman_sophomore_count - pet_owners

    result = non_pet_owners
    return result

print(solution())
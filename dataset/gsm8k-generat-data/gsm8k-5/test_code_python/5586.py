def solution():
    total_students = 400  # There are 400 students in the high school
    percent_fresh_soph = 0.5  # 50 percent of students are freshmen or sophomores
    fresh_soph_students = int(total_students * percent_fresh_soph)  # Calculate the number of freshmen and sophomores
    pet_owners_percent = 0.2  # 1/5 of freshmen and sophomores own a pet
    pet_owners = int(fresh_soph_students * pet_owners_percent)  # Calculate the number of pet owners among freshmen and sophomores

    # Calculate the number of freshmen and sophomores who do not own a pet
    non_pet_owners = fresh_soph_students - pet_owners
    result = non_pet_owners
    return result

print(solution())
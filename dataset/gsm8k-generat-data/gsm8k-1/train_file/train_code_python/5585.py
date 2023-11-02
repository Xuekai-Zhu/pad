def solution():
    """There are 400 students in a local high school. 50 percent are freshmen or sophomores. 1/5 of freshmen and sophomores own a pet. How many freshmen and sophomores do not own a pet?"""
    total_students = 400
    percent_frosh_soph = 50
    frosh_soph_students = total_students * (percent_frosh_soph / 100)
    pet_owners = frosh_soph_students * (1/5)
    non_pet_owners = frosh_soph_students - pet_owners
    result = non_pet_owners
    
    return result

print(solution())
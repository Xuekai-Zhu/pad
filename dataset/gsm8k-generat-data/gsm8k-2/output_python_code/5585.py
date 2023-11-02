def solution():
    """There are 400 students in a local high school. 50 percent are freshmen or sophomores. 1/5 of freshmen and sophomores own a pet. How many freshmen and sophomores do not own a pet?"""
    total_students = 400
    num_fresh_soph = total_students * 0.5
    num_pets = num_fresh_soph * 0.2
    num_no_pets = num_fresh_soph - num_pets
    result = num_no_pets
    return result

print(solution())
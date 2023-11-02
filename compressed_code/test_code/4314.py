def solution():
    
    total_students = 400
    num_fresh_soph = total_students * 0.5
    num_pets = num_fresh_soph * 0.2
    num_no_pets = num_fresh_soph - num_pets
    result = num_no_pets
    return result

print(solution())
def solution():
    
    total_students = 40
    puppies_percentage = 80
    parrots_percentage = 25
    students_with_puppies = total_students * (puppies_percentage / 100)
    students_with_puppies_and_parrots = students_with_puppies * (parrots_percentage / 100)
    result = students_with_puppies_and_parrots
    
    return result

print(solution())
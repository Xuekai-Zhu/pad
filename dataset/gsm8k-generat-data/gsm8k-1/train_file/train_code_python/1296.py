def solution():
    """In Professor Plum's biology class there are 40 students. Of those students, 80 percent have puppies. Of those who have puppies, 25% also have parrots. How many students have both puppies and parrots?"""
    total_students = 40
    puppies_percentage = 80
    parrots_percentage = 25
    students_with_puppies = total_students * (puppies_percentage / 100)
    students_with_puppies_and_parrots = students_with_puppies * (parrots_percentage / 100)
    result = students_with_puppies_and_parrots
    
    return result

print(solution())
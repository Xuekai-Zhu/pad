def solution():
    """In a classroom there are 30 students. 1/3 of them are boys. Among the girls, 40% own dogs, 20% own a cat, and the rest have no pets. How many girls in the class have no pet?"""
    total_students = 30
    boys = total_students // 3
    girls = total_students - boys
    girls_with_dogs = int(0.4 * girls)
    girls_with_cats = int(0.2 * girls)
    girls_with_pets = girls_with_dogs + girls_with_cats
    girls_with_no_pet = girls - girls_with_pets
    result = girls_with_no_pet
    
    return result

print(solution())
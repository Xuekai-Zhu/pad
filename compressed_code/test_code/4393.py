def solution():
    
    total_students = 30
    boys = total_students // 3
    girls = total_students - boys
    girls_with_dogs = 0.4 * girls
    girls_with_cats = 0.2 * girls
    girls_with_pets = girls_with_dogs + girls_with_cats
    girls_with_no_pets = girls - girls_with_pets
    result = girls_with_no_pets
    return result

print(solution())
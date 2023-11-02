def solution():
    total_students = 30  # There are 30 students in the class
    boys = total_students // 3  # 1/3 of the students are boys
    girls = total_students - boys  # The remaining students are girls
    girls_with_dogs = int(0.4 * girls)  # 40% of the girls own dogs
    girls_with_cats = int(0.2 * girls)  # 20% of the girls own cats
    girls_with_no_pets = girls - girls_with_dogs - girls_with_cats  # The rest of the girls have no pets
    result = girls_with_no_pets
    return result

print(solution())
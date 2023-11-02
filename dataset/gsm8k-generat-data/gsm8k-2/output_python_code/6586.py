def solution():
    """A school has 100 students. Half of the students are girls, the other half are boys. 20% of the girls have dogs at home and 10% of the boys have dogs at home. How many students own dogs?"""
    total_students = 100
    girls = total_students // 2
    boys = total_students // 2
    girls_with_dogs = 0.2 * girls
    boys_with_dogs = 0.1 * boys
    total_with_dogs = girls_with_dogs + boys_with_dogs
    result = total_with_dogs
    return result

print(solution())
def solution():
    """A school has 100 students. Half of the students are girls, the other half are boys. 20% of the girls have dogs at home and 10% of the boys have dogs at home. How many students own dogs?"""
    total_students = 100
    girls = total_students/2
    boys = total_students/2
    girl_dog_owners = 0.2*girls
    boy_dog_owners = 0.1*boys
    total_dog_owners = girl_dog_owners + boy_dog_owners
    result = total_dog_owners
    return result

print(solution())
def solution():
    """A school has 100 students. Half of the students are girls, the other half are boys. 20% of the girls have dogs at home and 10% of the boys have dogs at home. How many students own dogs?"""
    # Define the total number of students
    total_students = 100

    # Calculate the number of girls and boys
    girls = total_students // 2
    boys = total_students // 2

    # Calculate the number of girls and boys with dogs
    girls_with_dogs = girls * 0.2
    boys_with_dogs = boys * 0.1

    # Calculate the total number of students with dogs
    students_with_dogs = girls_with_dogs + boys_with_dogs

    result = int(students_with_dogs)
    return result

print(solution())
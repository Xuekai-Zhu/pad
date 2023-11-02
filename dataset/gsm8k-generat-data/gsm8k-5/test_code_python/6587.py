def solution():
    total_students = 100  # There are 100 students in the school
    girls = total_students / 2  # Half of the students are girls
    boys = total_students / 2  # The other half are boys

    # Calculate the number of girls who have dogs at home
    girls_with_dogs = 0.2 * girls

    # Calculate the number of boys who have dogs at home
    boys_with_dogs = 0.1 * boys

    # Calculate the total number of students who have dogs
    total_with_dogs = girls_with_dogs + boys_with_dogs
    result = total_with_dogs
    return result

print(solution())
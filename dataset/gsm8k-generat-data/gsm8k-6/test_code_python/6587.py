def solution():
    # Calculate the number of girls and boys in the school
    num_girls = 100 / 2
    num_boys = 100 / 2

    # Calculate the number of girls and boys who have dogs at home
    girls_with_dogs = 0.2 * num_girls
    boys_with_dogs = 0.1 * num_boys

    # Calculate the total number of students who own dogs
    total_with_dogs = girls_with_dogs + boys_with_dogs
    result = total_with_dogs
    return result

print(solution())
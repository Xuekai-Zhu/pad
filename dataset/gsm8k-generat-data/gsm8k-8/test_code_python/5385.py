def solution():
    # Calculate the number of girls based on the given ratio
    boys_to_girls_ratio = 3/4
    girls = 60
    boys = int(girls / boys_to_girls_ratio)

    # Calculate the number of teachers, assuming they are 20% of the boys
    teachers = int(0.2 * boys)

    # Calculate the total number of people at the dance
    total_people = girls + boys + teachers
    result = total_people
    return result

print(solution())
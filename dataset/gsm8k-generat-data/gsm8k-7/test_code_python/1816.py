def solution():
    num_dogs = 2
    num_people = 1

    # Calculate the total number of legs of the dogs
    dog_legs = num_dogs * 4

    # Calculate the total number of legs of the people
    people_legs = num_people * 2

    # Calculate the total number of legs of all organisms
    total_legs = dog_legs + people_legs
    result = total_legs
    return result

print(solution())
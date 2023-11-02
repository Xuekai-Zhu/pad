def solution():
    # Define the age of the dog in dog years
    dog_age = 10

    # Calculate the age of the dog in human years
    if dog_age == 1:
        human_age = 15
    elif dog_age == 2:
        human_age = 15 + 9
    else:
        human_age = 15 + 9 + (dog_age - 2) * 5

    result = human_age
    return result

print(solution())
def solution():
    # Calculate the ages of the dogs
    first_dog_age = 10
    second_dog_age = first_dog_age - 2
    third_dog_age = second_dog_age + 4
    fourth_dog_age = third_dog_age / 2
    fifth_dog_age = fourth_dog_age + 20

    # Calculate the sum of the ages of the first and fifth fastest dogs
    sum_ages = first_dog_age + fifth_dog_age

    # Calculate the average age of the first and fifth fastest dogs
    average_age = sum_ages / 2
    result = average_age
    return result

print(solution())
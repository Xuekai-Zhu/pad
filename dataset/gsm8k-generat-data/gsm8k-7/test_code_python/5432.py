def solution():
    first_dog_age = 10
    second_dog_age = first_dog_age - 2
    third_dog_age = second_dog_age + 4
    fourth_dog_age = third_dog_age / 2
    fifth_dog_age = fourth_dog_age + 20

    # Find the average of the first and fifth dog's ages
    avg_age = (first_dog_age + fifth_dog_age) / 2
    result = avg_age
    return result

print(solution())
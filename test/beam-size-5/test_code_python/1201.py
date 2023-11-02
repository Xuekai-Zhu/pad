def solution():
    num_dogs = 4
    miles_per_dog_1 = 1
    miles_per_dog_2 = 4
    miles_per_dog_3 = 3
    miles_per_day_1 = miles_per_dog_1 + miles_per_dog_2
    miles_per_day_2 = miles_per_dog_3
    miles_per_day_3 = miles_per_dog_3

    # Calculate the total miles needed for all dogs for the first two dogs
    total_miles_first_two_dogs = miles_per_dog_1 + miles_per_dog_2 + miles_per_day_3

    # Calculate the total miles needed for all dogs for the last dog
    total_miles_last_dog = total_miles_first_two_dogs + miles_per_day_3

    result = total_miles_last_dog
    return result

print(solution())
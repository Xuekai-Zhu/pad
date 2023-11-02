def solution():
    total_nails_trimmed = 164  # Carly trimmed 164 nails in total
    nails_per_dog = 4  # Carly trimmed 4 nails per dog
    dogs_with_three_legs = 3  # Carly worked on 3 dogs with only 3 legs

    # Calculate the total number of dogs Carly worked on
    total_dogs = (total_nails_trimmed - (nails_per_dog * dogs_with_three_legs)) / nails_per_dog
    result = total_dogs
    return result

print(solution())
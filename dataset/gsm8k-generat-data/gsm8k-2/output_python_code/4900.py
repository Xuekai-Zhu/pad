def solution():
    """My dog was born when I was 15 years old. Two years from now, my dog will turn 4 years old. How old am I now?"""
    dog_age = 4
    dog_birth_year = dog_age - 2
    my_birth_year = 15 - dog_birth_year
    my_age = my_birth_year + 2
    result = my_age
    return result

print(solution())
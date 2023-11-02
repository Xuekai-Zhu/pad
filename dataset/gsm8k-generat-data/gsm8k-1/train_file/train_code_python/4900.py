def solution():
    """My dog was born when I was 15 years old. Two years from now, my dog will turn 4 years old. How old am I now?"""
    dog_age = 2 + 4  # Two years from now, the dog will be 4 years old
    my_age_when_dog_was_born = 15
    my_current_age = my_age_when_dog_was_born + dog_age
    result = my_current_age
    return result

print(solution())
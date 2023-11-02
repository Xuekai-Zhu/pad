def solution():
    dog_age = 4    # age of dog in 2 years from now
    my_age_when_dog_was_born = 15 - 2   # age when dog was born
    my_current_age = my_age_when_dog_was_born + dog_age
    result = my_current_age
    return result

print(solution())
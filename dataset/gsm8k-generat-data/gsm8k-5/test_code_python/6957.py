def solution():
    dog_age = 10  # The dog is 10 years old
    
    if dog_age == 1:
        human_age = 15
    elif dog_age == 2:
        human_age = 15 + 9
    elif dog_age > 2:
        human_age = 15 + 9 + ((dog_age - 2) * 5)

    result = human_age
    return result

print(solution())
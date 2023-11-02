def solution():
    dog_age = 10  # age of dog in years
    human_age = 15  # human equivalent of dog's first year
    if dog_age == 1:  # if the dog is one year old
        human_age = 15
    elif dog_age == 2:  # if the dog is two years old
        human_age = 15 + 9
    else:  # if the dog is older than two years
        human_age = 15 + 9 + ((dog_age-2)*5)
    result = human_age
    return result

print(solution())
def solution():
    """They say the first year of a dog's life equals 15 human years. The second year of a dog's life equals 9 human years and after that, every year of a dog's life equals 5 human years. According to this logic, how many human years has my 10-year-old dog lived?"""
    dog_age = 10
    if dog_age == 1:
        human_age = 15
    elif dog_age == 2:
        human_age = 15 + 9
    else:
        human_age = 15 + 9 + ((dog_age - 2) * 5)
    result = human_age
    return result

print(solution())
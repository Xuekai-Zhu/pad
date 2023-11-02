def solution():
    animal_type = "dog"
    number_of_legs = 4
    if animal_type == "dog" and number_of_legs != 2:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
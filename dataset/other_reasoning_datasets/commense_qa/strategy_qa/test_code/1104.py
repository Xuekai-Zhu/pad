def solution():
    snickers_contains_chocolate = True
    chocolate_harmful_to_dogs = True
    breed_of_dog = "Poodle"
    if snickers_contains_chocolate and chocolate_harmful_to_dogs and breed_of_dog == "Poodle":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
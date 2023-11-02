def solution():
    dogs = 6  # There are 6 dogs
    ducks = 2  # There are 2 ducks
    legs_per_dog = 4  # Each dog has 4 legs
    legs_per_duck = 2  # Each duck has 2 legs

    # Calculate the total number of legs in the garden
    total_legs = (dogs * legs_per_dog) + (ducks * legs_per_duck)

    result = total_legs
    return result

print(solution())
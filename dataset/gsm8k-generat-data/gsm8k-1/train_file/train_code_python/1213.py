def solution():
    """Adlai has 2 dogs and 1 chicken. How many animal legs are there in all?"""
    dogs = 2
    chicken = 1
    legs_per_dog = 4
    legs_per_chicken = 2
    total_legs = (dogs * legs_per_dog) + (chicken * legs_per_chicken)
    result = total_legs
    return result

print(solution())
def solution():
    # Calculate the number of dogs standing on their back legs
    back_legs_dogs = 12 / 2

    # Calculate the number of dog paws on the ground
    paws_on_ground = (back_legs_dogs * 2) + ((12 - back_legs_dogs) * 4)

    result = paws_on_ground
    return result

print(solution())
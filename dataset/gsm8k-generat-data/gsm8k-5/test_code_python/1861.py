def solution():
    # Calculate the number of cats on the street
    cats = (2/3) * 300  # Two-thirds of the animals on the street are cats

    # Calculate the number of dogs on the street
    dogs = 300 - cats  # The rest of the animals are dogs

    # Calculate the total number of dog legs
    dog_legs = dogs * 4  # Each dog has 4 legs

    result = dog_legs
    return result

print(solution())
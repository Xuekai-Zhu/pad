def solution():
    # Calculate the total number of cats on the street
    total_cats = 300 * (2/3)

    # Calculate the number of dogs on the street
    total_dogs = 300 - total_cats

    # Calculate the total number of legs of dogs on the street
    total_dog_legs = total_dogs * 4

    result = total_dog_legs
    return result

print(solution())
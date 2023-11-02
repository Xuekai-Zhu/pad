def solution():
    """Madison takes her dog to the dog park. Counting Madison's dog, half the dogs have spots and 1/5 have pointy ears. If 15 dogs have spots, how many have pointy ears?"""
    # Define the number of dogs with spots
    dogs_with_spots = 15

    # Calculate the total number of dogs
    total_dogs = dogs_with_spots * 2

    # Calculate the number of dogs with pointy ears
    dogs_with_pointy_ears = total_dogs * (1/5)

    # Round the result to the nearest whole number
    result = round(dogs_with_pointy_ears)
    return result

print(solution())
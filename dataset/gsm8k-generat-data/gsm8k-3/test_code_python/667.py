def solution():
    """Madison takes her dog to the dog park. Counting Madison's dog, half the dogs have spots and 1/5 have pointy ears. If 15 dogs have spots, how many have pointy ears?"""
    # Define the number of dogs with spots and the ratio of dogs with pointy ears
    spots = 15
    pointy_ears_ratio = 1/5

    # Calculate the total number of dogs
    total_dogs = spots * 2 # since half the dogs have spots, there are twice as many dogs as spots

    # Calculate the number of dogs with pointy ears
    pointy_ears = int(total_dogs * pointy_ears_ratio) # use int() to round down to nearest whole number

    # Display the number of dogs with pointy ears
    result = pointy_ears
    return result

print(solution())
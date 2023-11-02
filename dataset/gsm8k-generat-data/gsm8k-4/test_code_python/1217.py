def solution():
    """Camden just bought 3/4 times as many dogs as Rico, who has 10 more dogs than Justin. If Justin has 14 dogs, what's the total number of legs that Camden's dogs have?"""
    # Define the number of dogs owned by Justin
    justin_dogs = 14

    # Define the number of dogs owned by Rico
    rico_dogs = justin_dogs + 10

    # Define the number of dogs owned by Camden
    camden_dogs = (3/4) * rico_dogs

    # Calculate the total number of legs of Camden's dogs
    total_legs = camden_dogs * 4

    result = total_legs
    return result

print(solution())
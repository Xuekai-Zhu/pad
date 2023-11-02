def solution():
    """Mariel is a dog walker. While walking her pack of dogs, she gets tangled up in the leashes of another dog walker and their 3 dogs. There are 36 legs tangled up in leashes. How many dogs is Mariel walking?"""
    # Define the number of legs of a dog
    LEGS_PER_DOG = 4

    # Define the number of other dogs and their legs
    other_dogs = 3
    other_legs = other_dogs * LEGS_PER_DOG

    # Calculate the total number of legs tangled up in leashes
    total_legs = 36 + other_legs

    # Calculate the number of dogs Mariel is walking
    Mariel_dogs = total_legs / LEGS_PER_DOG - other_dogs

    result = Mariel_dogs
    return result

print(solution())
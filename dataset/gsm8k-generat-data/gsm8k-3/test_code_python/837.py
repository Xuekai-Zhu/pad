def solution():
    """Mariel is a dog walker. While walking her pack of dogs, she gets tangled up in the leashes of another dog walker and their 3 dogs. There are 36 legs tangled up in leashes. How many dogs is Mariel walking?"""
    # Define the number of legs per dog
    LEGS_PER_DOG = 4

    # Calculate the number of Mariel's dogs
    mariel_dogs = (36 - (3 * LEGS_PER_DOG)) // LEGS_PER_DOG

    # Display the number of dogs Mariel is walking
    result = mariel_dogs
    return result

print(solution())
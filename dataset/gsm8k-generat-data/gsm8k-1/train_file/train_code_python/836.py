def solution():
    """Mariel is a dog walker. While walking her pack of dogs, she gets tangled up in the leashes of another dog walker and their 3 dogs. There are 36 legs tangled up in leashes. How many dogs is Mariel walking?"""
    mariel_dogs = 4  # including Mariel's own dog
    other_dogs = 3
    legs_per_dog = 4
    total_legs = mariel_dogs * legs_per_dog + other_dogs * legs_per_dog
    tangled_legs = 36
    Mariel_dogs = (tangled_legs - other_dogs * legs_per_dog) / legs_per_dog
    return Mariel_dogs

print(solution())
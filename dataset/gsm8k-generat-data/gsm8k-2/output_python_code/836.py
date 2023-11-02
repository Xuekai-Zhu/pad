def solution():
    """Mariel is a dog walker. While walking her pack of dogs, she gets tangled up in the leashes of another dog walker and their 3 dogs. There are 36 legs tangled up in leashes. How many dogs is Mariel walking?"""
    mariel_dogs = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if (4*i) + (4*j) == 36 and i != j:
                mariel_dogs = i
    result = mariel_dogs
    return result

print(solution())
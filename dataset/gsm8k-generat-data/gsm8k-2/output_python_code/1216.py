def solution():
    """Camden just bought 3/4 times as many dogs as Rico, who has 10 more dogs than Justin. If Justin has 14 dogs, what's the total number of legs that Camden's dogs have?"""
    justin_dogs = 14
    rico_dogs = justin_dogs + 10
    camden_dogs = (3/4) * rico_dogs
    total_legs = 4 * (justin_dogs + rico_dogs + camden_dogs)
    result = total_legs
    return result

print(solution())
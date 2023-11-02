def solution():
    justin_dogs = 14
    rico_dogs = justin_dogs + 10
    camden_dogs = (3/4) * rico_dogs

    # Each dog has 4 legs, so find the total number of legs for all of Camden's dogs
    total_legs = camden_dogs * 4
    result = total_legs
    return result

print(solution())
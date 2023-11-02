def solution():
    justin_dogs = 14  # Justin has 14 dogs
    rico_dogs = justin_dogs + 10  # Rico has 10 more dogs than Justin
    camden_dogs = (3/4) * rico_dogs  # Camden bought 3/4 times as many dogs as Rico

    # Calculate the total number of legs that Camden's dogs have
    total_legs = camden_dogs * 4
    result = total_legs
    return result

print(solution())
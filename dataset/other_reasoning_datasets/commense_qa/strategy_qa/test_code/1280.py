def solution():
    hound_breeds = ["Basenji", "Dachsund", "Beagle"]
    snoopys_breed = "Beagle"
    if snoopys_breed in hound_breeds:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
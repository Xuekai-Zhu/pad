def solution():
    bin_laden_religion = "Islam"
    islamic_prohibition = "alcohol consumption"
    if islamic_prohibition in bin_laden_religion.lower():
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
def solution():
    andes_peak_height = 23000
    colossus_height = 108
    andes_location = "South America"
    colossus_location = "ancient Greece"
    if andes_peak_height > colossus_height:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
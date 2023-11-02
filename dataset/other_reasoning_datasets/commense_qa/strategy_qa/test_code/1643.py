def solution():
    digital_object = "Bing"
    physical_object = "basket"
    if digital_object not in physical_object:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
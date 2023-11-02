def solution():
    joey_size = 2.0 # In centimeters
    nickel_diameter = 2.12 # In centimeters
    if joey_size < nickel_diameter:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
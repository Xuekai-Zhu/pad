def solution():
    sandwich_contents = ["Vegemite"]
    fish_types = ["Atlantic cod"]
    overlap = [food for food in sandwich_contents if food in fish_types]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
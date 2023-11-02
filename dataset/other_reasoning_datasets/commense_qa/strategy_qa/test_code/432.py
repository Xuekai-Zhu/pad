def solution():
    ford_vehicles = ["Mustang", "F-150", "Explorer"]
    ford_logo = "Ford"
    if ford_logo in "".join(ford_vehicles):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
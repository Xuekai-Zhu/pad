def solution():
    army_size = 780000
    ship_capacity = 5518
    if army_size <= ship_capacity:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
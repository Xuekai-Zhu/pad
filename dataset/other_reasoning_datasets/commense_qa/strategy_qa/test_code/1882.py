def solution():
    num_wives = 4
    num_seats = 4
    if num_wives <= num_seats:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
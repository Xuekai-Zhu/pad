def solution():
    num_chief_justices = 17
    max_seats_on_boeing = 215
    if num_chief_justices <= max_seats_on_boeing:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
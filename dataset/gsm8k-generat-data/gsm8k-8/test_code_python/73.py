def solution():
    # Calculate the total number of people who need a snack
    total_people = 13 + 3 + 2

    # Calculate the total number of pouches needed
    total_pouches = total_people / 6

    # Round up to the nearest whole number of packs
    packs_needed = math.ceil(total_pouches)
    result = packs_needed
    return result

print(solution())
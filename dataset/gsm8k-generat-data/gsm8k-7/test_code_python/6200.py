def solution():
    total_houses = 2000
    built_houses_first_half = (3/5) * total_houses
    additional_houses_by_october = 300

    # Calculate the total number of houses built
    total_built_houses = built_houses_first_half + additional_houses_by_october

    # Calculate the number of houses still remaining to be built
    houses_remaining = total_houses - total_built_houses
    result = houses_remaining
    return result

print(solution())
def solution():
    number_of_houses = 2000
    first_half = 3/5
    second_half = 300
    total_built = first_half + second_half
    remaining = number_of_houses - total_built
    result = remaining
    return result

print(solution())
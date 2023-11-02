def solution():
    population = 300
    num_vampires = 2
    num_nights = 2

    # Each vampire turns 5 more people into vampires every night
    for night in range(num_nights):
        num_vampires *= 6

    result = num_vampires
    return result

print(solution())
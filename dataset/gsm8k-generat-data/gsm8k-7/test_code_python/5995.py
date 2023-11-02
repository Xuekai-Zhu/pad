def solution():
    mary_sheep = 300
    bob_sheep = (2*mary_sheep) + 35
    difference = 69

    # Calculate how many sheep Mary needs to have the same number as Bob
    needed_sheep = (bob_sheep - difference) - mary_sheep

    result = needed_sheep
    return result

print(solution())
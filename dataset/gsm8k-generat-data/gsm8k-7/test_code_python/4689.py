def solution():
    benjamin_eggs = 6 * 12
    carla_eggs = 3 * benjamin_eggs
    trisha_eggs = (6 - 4) * 12

    # Calculate the total number of dozen eggs collected by all three
    total_dozen_eggs = (benjamin_eggs + carla_eggs + trisha_eggs) / 12
    result = total_dozen_eggs
    return result

print(solution())
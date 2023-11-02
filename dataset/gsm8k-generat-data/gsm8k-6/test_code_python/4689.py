def solution():
    # Calculate the number of dozen eggs collected by each person
    benjamin_eggs = 6 * 12  # Benjamin collects 6 dozen eggs
    carla_eggs = 3 * benjamin_eggs  # Carla collects 3 times the number of eggs that Benjamin collects
    trisha_eggs = (6 - 4) * 12  # Trisha collects 4 dozen less than Benjamin
    total_eggs = (benjamin_eggs + carla_eggs + trisha_eggs) / 12  # Divide by 12 to convert to dozens

    result = total_eggs
    return result

print(solution())
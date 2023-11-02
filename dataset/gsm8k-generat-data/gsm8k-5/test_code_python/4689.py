def solution():
    benjamin_eggs = 6 * 12  # Benjamin collects 6 dozen eggs a day, which is 6 * 12 = 72 eggs
    carla_eggs = 3 * benjamin_eggs  # Carla collects 3 times the number of eggs that Benjamin collects
    trisha_eggs = benjamin_eggs - (4 * 12)  # Trisha collects 4 dozen less than Benjamin, which is 4 * 12 = 48 eggs less

    # Calculate the total number of eggs collected by the three
    total_eggs = benjamin_eggs + carla_eggs + trisha_eggs

    # Convert the total number of eggs to dozens of eggs
    dozens_of_eggs = total_eggs / 12
    result = dozens_of_eggs
    return result

print(solution())
def solution():
    # Define the starting number of vampires
    vampires = 2

    # Define the number of people in the village
    population = 300

    # Calculate the number of new vampires after the first night
    new_vampires = vampires * 5

    # Update the total number of vampires
    vampires += new_vampires

    # Calculate the number of new vampires after the second night
    new_vampires = vampires * 5

    # Update the total number of vampires
    vampires += new_vampires

    result = vampires
    return result

print(solution())
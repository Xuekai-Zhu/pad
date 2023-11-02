def solution():
    """Two vampires have come to the sleepy village of Willowton, population 300. Every night, each vampire turns 5 more people into vampires. How many vampires are there after two nights?"""
    # Define the initial number of vampires and population
    vampires = 2
    population = 300

    # Calculate the number of new vampires after one night
    new_vampires = vampires * 5

    # Calculate the total number of vampires after one night
    total_vampires = vampires + new_vampires

    # Calculate the number of new vampires after two nights
    new_vampires_2 = total_vampires * 5

    # Calculate the total number of vampires after two nights
    total_vampires_2 = total_vampires + new_vampires_2

    # Display the total number of vampires after two nights
    result = total_vampires_2
    return result

print(solution())
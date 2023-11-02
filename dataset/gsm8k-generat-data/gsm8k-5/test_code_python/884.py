def solution():
    initial_vampires = 2  # There are initially 2 vampires
    population = 300  # The village has a population of 300

    # Calculate the number of vampires after one night
    vampires_after_one_night = initial_vampires + (5 * population)

    # Calculate the number of vampires after two nights
    vampires_after_two_nights = vampires_after_one_night + (5 * population)

    result = vampires_after_two_nights
    return result

print(solution())
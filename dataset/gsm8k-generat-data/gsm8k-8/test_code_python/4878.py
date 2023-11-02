def solution():
    # Define the starting number of plants
    starting_plants = 30

    # Calculate the number of plants after the first wave of bugs
    first_wave = starting_plants - 20

    # Calculate the number of plants after the second wave of bugs
    second_wave = (1/2) * first_wave

    # Calculate the number of plants after the third wave of bugs
    third_wave = second_wave - 1

    result = third_wave
    return result

print(solution())
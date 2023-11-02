def solution():
    
    # Define the initial number of penguins
    initial_penguins = 36

    # Calculate the number of penguins that jump in and swim in the ocean
    jump_in_ocean = initial_penguins // 3

    # Calculate the number of penguins that go inside the cave
    dinner_in_cave = initial_penguins // 3

    # Calculate the number of penguins that still left sunbathing
    sunbathing_left = initial_penguins - jump_in_ocean - dinner_in_cave

    # Display the number of penguins still sunbathing
    result = sunbathing_left
    return result

print(solution())
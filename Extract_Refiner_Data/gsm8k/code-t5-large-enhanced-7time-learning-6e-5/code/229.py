def solution():
    
    # Define the initial number of sunbathing penguins
    initial_sunbathing = 36

    # Calculate the number of sunbathing penguins that jump in and swim in the ocean
    ocean_sunbathing = initial_sunbathing // 3

    # Calculate the number of sunbathing penguins that go inside the cave to eat their dinner
    dinner_sunbathing = initial_sunbathing // 3

    # Calculate the number of sunbathing penguins that are still left sunbathing
    sunbathing_left = initial_sunbathing - ocean_sunbathing - dinner_sunbathing

    # return the result
    result = sunbathing_left
    return result

print(solution())
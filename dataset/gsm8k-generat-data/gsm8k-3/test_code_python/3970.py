def solution():
    """Carla adds a can of chilis, two cans of beans, and 50% more tomatoes than beans to a normal batch of chili.
    If she makes a quadruple batch, how many cans of food does she need?"""
    # Define the number of cans needed for a normal batch of chili
    CHILIS_PER_BATCH = 1
    BEANS_PER_BATCH = 2
    TOMATOES_PER_BATCH = BEANS_PER_BATCH * 1.5

    # Calculate the number of cans needed for a quadruple batch of chili
    cans_chilis = CHILIS_PER_BATCH * 4
    cans_beans = BEANS_PER_BATCH * 4
    cans_tomatoes = TOMATOES_PER_BATCH * 4

    # Calculate the total number of cans needed
    total_cans = cans_chilis + cans_beans + cans_tomatoes

    # Display the total number of cans needed
    result = total_cans
    return result

print(solution())
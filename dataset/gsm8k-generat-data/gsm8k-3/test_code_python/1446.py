def solution():
    """A clothing store has an inventory of 34 ties, 40 belts, 63 black shirts, and 42 white shirts. The number of jeans in the store is two-thirds of the sum of black and white shirts, and the number of scarves is half the number of the sum of ties and belts. How many more jeans are there than scarves?"""
    # Define the inventory numbers
    ties = 34
    belts = 40
    black_shirts = 63
    white_shirts = 42

    # Calculate the number of jeans
    jeans = int((black_shirts + white_shirts) * 2 / 3)

    # Calculate the number of scarves
    scarves = int((ties + belts) / 2)

    # Calculate the difference between the number of jeans and scarves
    difference = jeans - scarves

    # Display the difference
    result = difference
    return result

print(solution())
def solution():
    """Carter has a jar with 20 green M&Ms and 20 red M&Ms. He eats 12 of the green M&Ms, then his sister comes and eats half the red M&Ms and adds 14 yellow M&Ms. If Carter picks an M&M at random now, what is the percentage chance he'll get a green M&M?"""
    # Define the initial number of green and red M&Ms
    initial_green = 20
    initial_red = 20

    # Define the number of M&Ms that are taken out
    removed_green = 12
    removed_red = initial_red / 2

    # Define the number of M&Ms that are added
    added_yellow = 14

    # Calculate the number of remaining green and red M&Ms
    remaining_green = initial_green - removed_green
    remaining_red = initial_red - removed_red

    # Calculate the total number of M&Ms
    total_MMs = remaining_green + remaining_red + added_yellow

    # Calculate the percentage chance of selecting a green M&M
    chance_green = (remaining_green / total_MMs) * 100

    # Display the percentage chance of selecting a green M&M
    result = chance_green
    return result

print(solution())
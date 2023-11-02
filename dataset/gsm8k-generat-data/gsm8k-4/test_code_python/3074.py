def solution():
    """Carter has a jar with 20 green M&Ms and 20 red M&Ms. He eats 12 of the green M&Ms, then his sister comes and eats half the red M&Ms and adds 14 yellow M&Ms. If Carter picks an M&M at random now, what is the percentage chance he'll get a green M&M?"""
    # Define the initial number of green and red M&Ms
    green_initial = 20
    red_initial = 20

    # Subtract the M&Ms that Carter ate
    green_remaining = green_initial - 12

    # Calculate the number of red M&Ms remaining after Carter's sister eats half of them and adds 14 yellow M&Ms
    red_remaining = (red_initial / 2) - 14

    # Calculate the total number of remaining M&Ms
    total_remaining = green_remaining + red_remaining

    # Calculate the percentage chance of picking a green M&M
    green_percentage = (green_remaining / total_remaining) * 100

    result = green_percentage
    return result

print(solution())
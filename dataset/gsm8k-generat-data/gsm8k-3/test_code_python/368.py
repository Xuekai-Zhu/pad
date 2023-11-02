def solution():
    """Keaton climbed a 30 feet ladder twenty times while working at the construction site. Reece, also working at the same site, climbed a ladder 4 feet shorter than Keaton's ladder 15 times. What's the total length of the ladders that both workers climbed in inches?"""
    # Define the height of Keaton's ladder
    KEATON_HEIGHT = 30  # in feet

    # Define the number of times Keaton climbed the ladder
    keaton_climbs = 20

    # Define the height of Reece's ladder
    REESE_HEIGHT = KEATON_HEIGHT - 4  # in feet

    # Define the number of times Reese climbed the ladder
    reese_climbs = 15

    # Calculate the total height climbed by Keaton in inches
    keaton_total = KEATON_HEIGHT * 12 * keaton_climbs

    # Calculate the total height climbed by Reese in inches
    reese_total = REESE_HEIGHT * 12 * reese_climbs

    # Calculate the total height climbed by both workers in inches
    total_height = keaton_total + reese_total

    # Display the total height climbed
    result = total_height
    return result

print(solution())
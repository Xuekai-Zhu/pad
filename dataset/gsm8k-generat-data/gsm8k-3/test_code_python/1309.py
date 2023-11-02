def solution():
    """Martin has 18 goldfish. Each week 5 goldfish die. Martin purchases 3 new goldfish every week. How many goldfish will Martin have in 7 weeks?"""
    # Initialize number of goldfish
    goldfish = 18

    # Calculate number of goldfish after each week
    for i in range(7):
        goldfish = goldfish - 5 + 3  # subtract dead goldfish, add new goldfish

    # Display the final number of goldfish
    result = goldfish
    return result

print(solution())
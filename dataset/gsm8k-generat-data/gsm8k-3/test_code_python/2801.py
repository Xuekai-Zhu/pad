def solution():
    """Borgnine wants to see 1100 legs at the zoo. He has already seen 12 chimps, 8 lions, and 5 lizards. He is next headed to see the tarantulas. How many tarantulas does he need to see to meet his goal?"""
    # Define the number of legs on each type of animal
    chimp_legs = 2
    lion_legs = 4
    lizard_legs = 4
    tarantula_legs = 8

    # Define the number of each type of animal Borgnine has already seen
    chimp_count = 12
    lion_count = 8
    lizard_count = 5

    # Calculate the total number of legs on animals Borgnine has already seen
    total_legs_seen = chimp_count * chimp_legs + lion_count * lion_legs + lizard_count * lizard_legs

    # Calculate the number of tarantulas Borgnine needs to see to meet his goal
    tarantula_legs_needed = 1100 - total_legs_seen
    tarantula_count_needed = tarantula_legs_needed // tarantula_legs

    # Display the number of tarantulas Borgnine needs to see
    result = tarantula_count_needed
    return result

print(solution())
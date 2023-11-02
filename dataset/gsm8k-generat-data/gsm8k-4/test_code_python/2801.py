def solution():
    """Borgnine wants to see 1100 legs at the zoo. He has already seen 12 chimps, 8 lions, and 5 lizards. He is next headed to see the tarantulas. How many tarantulas does he need to see to meet his goal?"""
    # Define the number of legs Borgnine has already seen
    legs_seen = 12*2 + 8*4 + 5*4

    # Define the total number of legs Borgnine wants to see
    total_legs = 1100

    # Calculate the number of tarantulas Borgnine needs to see to meet his goal
    tarantulas_needed = (total_legs - legs_seen) / 8

    # Round up to the nearest integer
    tarantulas_needed = math.ceil(tarantulas_needed)

    # Return the result
    result = tarantulas_needed
    return result

print(solution())
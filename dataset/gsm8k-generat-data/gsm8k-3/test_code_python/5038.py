def solution():
    """There were 148 peanuts in a jar. Brock ate one-fourth of the peanuts and Bonita ate 29 peanuts. How many peanuts remain in the jar?"""
    # Initialize the number of peanuts in the jar
    peanuts_in_jar = 148

    # Calculate the number of peanuts Brock ate
    brock_peanuts = peanuts_in_jar / 4

    # Calculate the number of peanuts remaining after Brock ate
    remaining_peanuts = peanuts_in_jar - brock_peanuts

    # Subtract the number of peanuts Bonita ate
    remaining_peanuts -= 29

    # Display the number of peanuts remaining in the jar
    result = remaining_peanuts
    return result

print(solution())
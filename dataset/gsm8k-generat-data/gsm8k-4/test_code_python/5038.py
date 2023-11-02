def solution():
    """There were 148 peanuts in a jar. Brock ate one-fourth of the peanuts and Bonita ate 29 peanuts. How many peanuts remain in the jar?"""
    # Define the initial number of peanuts and the amount eaten by Brock and Bonita
    initial_peanuts = 148
    brock_eaten = initial_peanuts * 0.25
    bonita_eaten = 29

    # Calculate the remaining number of peanuts
    remaining_peanuts = initial_peanuts - brock_eaten - bonita_eaten

    result = remaining_peanuts
    return result

print(solution())
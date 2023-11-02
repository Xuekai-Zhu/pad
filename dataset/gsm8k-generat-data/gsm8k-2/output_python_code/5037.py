def solution():
    """There were 148 peanuts in a jar. Brock ate one-fourth of the peanuts and Bonita ate 29 peanuts. How many peanuts remain in the jar?"""
    initial_peanuts = 148
    brock_ate = initial_peanuts / 4
    bonita_ate = 29
    peanuts_left = initial_peanuts - brock_ate - bonita_ate
    result = peanuts_left
    return result

print(solution())
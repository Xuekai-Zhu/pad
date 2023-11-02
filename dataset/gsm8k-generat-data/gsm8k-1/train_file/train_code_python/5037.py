def solution():
    """There were 148 peanuts in a jar. Brock ate one-fourth of the peanuts and Bonita ate 29 peanuts. How many peanuts remain in the jar?"""
    total_peanuts = 148
    brock_share = total_peanuts / 4
    peanuts_left = total_peanuts - brock_share - 29
    result = peanuts_left
    return result

print(solution())
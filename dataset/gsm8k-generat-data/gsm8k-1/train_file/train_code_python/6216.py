def solution():
    """Levi has 5 lemons. Jayden has 6 more lemons than Levi. Jayden has one-third as many lemons as Eli has while Eli has one-half as many lemons as Ian has. How many lemons do they have in all?"""
    lemons_levi = 5
    lemons_jayden = lemons_levi + 6
    lemons_eli = lemons_jayden * 3
    lemons_ian = lemons_eli * 2
    total_lemons = lemons_levi + lemons_jayden + lemons_eli + lemons_ian
    result = total_lemons
    return result

print(solution())
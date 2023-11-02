def solution():
    lemons_Levi = 5
    lemons_Jayden = lemons_Levi + 6  # Jayden has 6 more lemons than Levi
    lemons_Eli = 3 * lemons_Jayden  # Jayden has one-third as many lemons as Eli
    lemons_Ian = 2 * lemons_Eli  # Eli has one-half as many lemons as Ian
    total_lemons = lemons_Levi + lemons_Jayden + lemons_Eli + lemons_Ian
    result = total_lemons
    return result

print(solution())
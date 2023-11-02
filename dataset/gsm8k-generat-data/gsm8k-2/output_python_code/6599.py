def solution():
    """Chef Michel made shepherd's pie cut into 4 pieces and chicken pot pie cut into 5 pieces for the lunch crowd. 52 customers ordered slices of shepherd's pie and 80 customers ordered slices of chicken pot pie. How many total pies did Chef Michel sell?"""
    shepherd_slices = 52
    pot_slices = 80
    shepherd_pies = shepherd_slices / 4
    pot_pies = pot_slices / 5
    total_pies = shepherd_pies + pot_pies
    result = total_pies
    return result

print(solution())
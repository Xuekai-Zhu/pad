def solution():
    """Chef Michel made shepherd's pie cut into 4 pieces and chicken pot pie cut into 5 pieces for the lunch crowd. 52 customers ordered slices of shepherd's pie and 80 customers ordered slices of chicken pot pie. How many total pies did Chef Michel sell?"""
    shepherd_pie_slices_per_pie = 4
    chicken_pot_pie_slices_per_pie = 5
    total_shepherd_pie_slices = 52
    total_chicken_pot_pie_slices = 80
    
    total_shepherd_pies = total_shepherd_pie_slices / shepherd_pie_slices_per_pie
    total_chicken_pot_pies = total_chicken_pot_pie_slices / chicken_pot_pie_slices_per_pie
    total_pies = total_shepherd_pies + total_chicken_pot_pies
    
    result = total_pies
    return result

print(solution())
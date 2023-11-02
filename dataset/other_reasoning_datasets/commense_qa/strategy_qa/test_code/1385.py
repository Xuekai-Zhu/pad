def solution():
    # Define viscosity and water's resistance to deformation
    viscosity = "resistance of fluid to deformation"
    water_resistance = "not resistant to deformation"
    # Check if water has viscosity
    if viscosity in water_resistance:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
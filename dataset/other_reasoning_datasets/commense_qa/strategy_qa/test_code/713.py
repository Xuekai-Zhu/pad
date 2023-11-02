def solution():
    shoebox_dimensions = [14, 10, 5] #in inches
    cell_diameter = 100 #in micrometers, assuming largest eukaryotic cell
    cell_radius = cell_diameter / 2
    shoebox_volume = shoebox_dimensions[0] * shoebox_dimensions[1] * shoebox_dimensions[2] #in cubic inches
    cell_volume = (4/3) * 3.14 * (cell_radius ** 3) #in cubic micrometers
    cell_volume_in_inches = cell_volume / (10 ** 12) #converting to cubic inches
    if cell_volume_in_inches <= shoebox_volume:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
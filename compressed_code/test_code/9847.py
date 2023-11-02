def solution():
    
    bed_length = 8
    bed_width = 4
    bed_height = 1
    soil_per_bed = bed_length * bed_width * bed_height
    total_soil = soil_per_bed * 2
    bags_of_soil = total_soil / 4
    result = bags_of_soil
    return result

print(solution())
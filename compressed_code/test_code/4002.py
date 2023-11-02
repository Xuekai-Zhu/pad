def solution():
    
    bed_length = 8
    bed_width = 4
    bed_height = 1
    soil_per_bag = 4
    total_cubic_feet = 2 * bed_length * bed_width * bed_height
    bags_of_soil = total_cubic_feet / soil_per_bag
    result = bags_of_soil
    return result

print(solution())
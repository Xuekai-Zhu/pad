def solution():
    """Abby is building 2 raised beds to grow vegetables. The beds are both 8 feet long, 4 feet wide and 1 foot high. Each bag of soil has 4 cubic feet. How many bags of soil will she need?"""
    bed_length = 8
    bed_width = 4
    bed_height = 1
    soil_per_bed = bed_length * bed_width * bed_height
    total_soil = soil_per_bed * 2
    bags_of_soil = total_soil / 4
    result = bags_of_soil
    return result

print(solution())
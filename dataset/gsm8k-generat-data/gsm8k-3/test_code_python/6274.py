def solution():
    """Jill is going to resod her front yard. The plot of land in front of her house is 200 feet wide by 50 feet. Her house has a sidewalk that is 3 feet wide and 50 feet long. There are also four flower beds: two right in front of the house that are 4 feet deep by 25 feet long, one that is 10 feet by 12 feet, and a fourth that is 7 feet by 8 feet. How many square feet of sod will she need to cover her yard, minus the sidewalk and flower beds?"""
    # Define the dimensions of the plot of land and sidewalk
    land_width = 200
    land_length = 50
    sidewalk_width = 3
    sidewalk_length = 50

    # Calculate the area of the plot of land and sidewalk
    land_area = land_width * land_length
    sidewalk_area = sidewalk_width * sidewalk_length

    # Define the dimensions of the flower beds
    bed1_width = 25
    bed1_length = 4
    bed2_width = 25
    bed2_length = 4
    bed3_width = 12
    bed3_length = 10
    bed4_width = 8
    bed4_length = 7

    # Calculate the area of the flower beds
    bed1_area = bed1_width * bed1_length
    bed2_area = bed2_width * bed2_length
    bed3_area = bed3_width * bed3_length
    bed4_area = bed4_width * bed4_length
    total_bed_area = bed1_area + bed2_area + bed3_area + bed4_area

    # Calculate the total area to be resodded
    total_area = land_area - sidewalk_area - total_bed_area

    # Display the total area
    result = total_area
    return result

print(solution())
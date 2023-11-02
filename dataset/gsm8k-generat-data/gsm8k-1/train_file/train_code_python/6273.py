def solution():
    """Jill is going to resod her front yard. The plot of land in front of her house is 200 feet wide by 50 feet. Her house has a sidewalk that is 3 feet wide and 50 feet long. There are also four flower beds: two right in front of the house that are 4 feet deep by 25 feet long, one that is 10 feet by 12 feet, and a fourth that is 7 feet by 8 feet. How many square feet of sod will she need to cover her yard, minus the sidewalk and flower beds?"""
    yard_width = 200
    yard_length = 50
    sidewalk_width = 3
    sidewalk_length = 50
    flower_bed_1_width = 4
    flower_bed_1_length = 25
    flower_bed_2_width = 4
    flower_bed_2_length = 25
    flower_bed_3_width = 10
    flower_bed_3_length = 12
    flower_bed_4_width = 7
    flower_bed_4_length = 8
    yard_area = yard_width * yard_length
    sidewalk_area = sidewalk_width * sidewalk_length
    flower_bed_1_area = flower_bed_1_width * flower_bed_1_length
    flower_bed_2_area = flower_bed_2_width * flower_bed_2_length
    flower_bed_3_area = flower_bed_3_width * flower_bed_3_length
    flower_bed_4_area = flower_bed_4_width * flower_bed_4_length
    total_area_to_cover = yard_area - sidewalk_area - flower_bed_1_area - flower_bed_2_area - flower_bed_3_area - flower_bed_4_area
    result = total_area_to_cover
    return result

print(solution())
def solution():
    
    yard_width = 200
    yard_length = 50
    sidewalk_width = 3
    sidewalk_length = 50
    flower_bed_1_width = 25
    flower_bed_1_length = 4
    flower_bed_2_width = 25
    flower_bed_2_length = 4
    flower_bed_3_width = 12
    flower_bed_3_length = 10
    flower_bed_4_width = 8
    flower_bed_4_length = 7

    yard_area = yard_width * yard_length
    sidewalk_area = sidewalk_width * sidewalk_length
    flower_bed_1_area = flower_bed_1_width * flower_bed_1_length
    flower_bed_2_area = flower_bed_2_width * flower_bed_2_length
    flower_bed_3_area = flower_bed_3_width * flower_bed_3_length
    flower_bed_4_area = flower_bed_4_width * flower_bed_4_length

    total_area = yard_area - sidewalk_area - flower_bed_1_area - flower_bed_2_area - flower_bed_3_area - flower_bed_4_area
    result = total_area
    return result

print(solution())
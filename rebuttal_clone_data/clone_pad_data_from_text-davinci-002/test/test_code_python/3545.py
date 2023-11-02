def solution():
    house_width = 200
    house_length = 50
    sidewalk_width = 3
    sidewalk_length = 50
    flower_bed_1_depth = 4
    flower_bed_1_length = 25
    flower_bed_2_depth = 4
    flower_bed_2_length = 25
    flower_bed_3_depth = 10
    flower_bed_3_length = 12
    flower_bed_4_depth = 7
    flower_bed_4_length = 8
    
    area_to_sod = (house_width * house_length) - (sidewalk_width * sidewalk_length) - ((flower_bed_1_depth * flower_bed_1_length) + (flower_bed_2_depth * flower_bed_2_length) + (flower_bed_3_depth * flower_bed_3_length) + (flower_bed_4_depth * flower_bed_4_length))
    result = area_to_sod
    
    return result

print(solution())
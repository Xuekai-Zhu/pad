def solution():
     house1_width = 1
     house1_height = 2
     house1_depth = 2
     house2_width = 16/12
     house2_height = 20/12
     house2_depth = 18/12
     house1_volume = house1_width * house1_height * house1_depth
     house2_volume = house2_width * house2_height * house2_depth
     volume_difference = house2_volume - house1_volume
     result = volume_difference
     return result

print(solution())
def solution():
     lamps = 20
     light_bulbs_per_lamp = 7
     lamps_with_burnt_out_bulbs = lamps / 4
     light_bulbs_burnt_out = lamps_with_burnt_out_bulbs * 2
     total_light_bulbs = lamps * light_bulbs_per_lamp
     light_bulbs_working = total_light_bulbs - light_bulbs_burnt_out
     result = light_bulbs_working
     return result

print(solution())
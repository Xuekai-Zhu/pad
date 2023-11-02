def solution():
     
     heavy_wash = 20
     regular_wash = 10
     light_wash = 2
     heavy_loads = 2
     regular_loads = 3
     light_loads = 1
     bleach_loads = 2
     total_water = (heavy_loads * heavy_wash) + (regular_loads * regular_wash) + (light_loads * light_wash) + (bleach_loads * light_wash)
     result = total_water
     return result

print(solution())
def solution():
    
    skins_per_coat = 15
    andy_minks = 30
    andy_minks_babies = andy_minks * 6
    total_minks = andy_minks + andy_minks_babies
    total_minks = int(total_minks / 2)  
    total_coats = int(total_minks / skins_per_coat)
    result = total_coats
    return result

print(solution())
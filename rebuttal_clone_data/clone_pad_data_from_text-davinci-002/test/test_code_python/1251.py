def solution():
     total_land = 150
     house_land = 25
     expansion_land = 15
     cattle_land = 40
     crop_land = total_land - house_land - expansion_land - cattle_land
     result = crop_land
     return result

print(solution())
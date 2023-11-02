def solution():
     hugo_mountain_elevation = 10000
     boris_mountain_elevation = hugo_mountain_elevation - 2500
     hugo_climbs = 3
     boris_climbs = hugo_climbs * (boris_mountain_elevation / hugo_mountain_elevation)
     result = boris_climbs
     return result

print(solution())
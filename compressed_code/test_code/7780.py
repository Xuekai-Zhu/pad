def solution():
    
    hugo_elevation = 10000
    boris_elevation = hugo_elevation - 2500
    hugo_climbs = 3
    boris_climbs = (hugo_climbs * hugo_elevation) / boris_elevation
    result = boris_climbs
    return result

print(solution())
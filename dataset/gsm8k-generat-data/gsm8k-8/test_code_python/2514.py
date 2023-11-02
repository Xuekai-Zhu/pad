def solution():
    hugo_elevation = 10000
    boris_elevation = hugo_elevation - 2500

    hugo_climbed = hugo_elevation * 3
    boris_climbed = hugo_climbed / boris_elevation

    result = boris_climbed
    return result

print(solution())
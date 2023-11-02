def solution():
    """Jamestown has 20 theme parks. If Venice has 25 more theme parks than Jamestown, and Marina Del Ray has 50 more theme parks than Jamestown, calculate the number of theme parks present in the three towns."""
    jamestown_parks = 20
    venice_parks = jamestown_parks + 25
    marina_del_ray_parks = jamestown_parks + 50
    total_parks = jamestown_parks + venice_parks + marina_del_ray_parks
    result = total_parks
    return result

print(solution())
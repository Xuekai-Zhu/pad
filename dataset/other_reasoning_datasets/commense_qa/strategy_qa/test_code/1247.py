def solution():
    publication_year = 1898
    cosmic_ray_discovery_year = 1912
    if publication_year < cosmic_ray_discovery_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
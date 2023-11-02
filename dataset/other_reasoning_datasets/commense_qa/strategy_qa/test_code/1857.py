def solution():
    olympic_year = 1984
    olympic_host = "Los Angeles, California"
    western_hemisphere = True
    if western_hemisphere and "Los Angeles" in olympic_host:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
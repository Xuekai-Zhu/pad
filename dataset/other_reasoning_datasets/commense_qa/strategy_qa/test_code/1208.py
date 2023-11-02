def solution():
    mickey_creation_year = 1928
    bugs_creation_year = 1930
    mickey_studio = "Disney"
    bugs_studio = "Warner Bros."
    if mickey_creation_year < bugs_creation_year and mickey_studio != bugs_studio:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
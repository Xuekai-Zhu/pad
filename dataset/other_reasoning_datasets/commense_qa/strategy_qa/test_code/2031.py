def solution():
    scientific_revolution_years = [16, 17]
    iphone_release_year = 21
    if iphone_release_year > max(scientific_revolution_years):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
def solution():
    harlem_renaissance_years = range(1920, 1930)
    al_capone_years = range(1899, 1947)
    overlap = any(year in al_capone_years for year in harlem_renaissance_years)
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
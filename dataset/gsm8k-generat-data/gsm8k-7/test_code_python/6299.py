def solution():
    year_started = 2006
    year_born = 1992
    years_fencing = 16

    # Calculate Ariel's current age
    current_year = datetime.datetime.now().year
    age = current_year - (year_born + years_fencing)
    result = age
    return result

print(solution())
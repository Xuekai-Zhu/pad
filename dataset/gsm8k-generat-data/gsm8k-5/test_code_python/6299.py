def solution():
    year_started_fencing = 2006
    year_born = 1992

    # Calculate Ariel's current age
    current_year = datetime.datetime.now().year
    years_fencing = current_year - year_started_fencing
    age = current_year - years_fencing - year_born

    result = age
    return result

print(solution())
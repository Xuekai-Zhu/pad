def solution():
    num_years = 4
    days_per_year = 365
    num_comics_per_day = 1
    days_per_comic = 2

    # Calculate the total number of days in 4 years
    total_days = num_years * days_per_year

    # Calculate the total number of comics James writes in 4 years
    num_comics = (total_days / days_per_comic) * num_comics_per_day
    result = num_comics
    return result

print(solution())
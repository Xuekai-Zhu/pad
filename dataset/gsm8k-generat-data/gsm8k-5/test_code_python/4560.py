def solution():
    days_in_year = 365  # Assuming there is no leap year
    days_in_4_years = days_in_year * 4  # Four years have 1460 days
    comics_every_other_day = days_in_4_years / 2  # James writes a comic every other day

    # Calculate the total number of comics James has written
    total_comics = comics_every_other_day
    result = total_comics
    return result

print(solution())
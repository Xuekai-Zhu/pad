def solution():
    boxer_rebellion_dates = ["1899-01-01", "1901-12-31"]
    royal_air_force_formation_date = "1918-04-01"
    if royal_air_force_formation_date < boxer_rebellion_dates[1]:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
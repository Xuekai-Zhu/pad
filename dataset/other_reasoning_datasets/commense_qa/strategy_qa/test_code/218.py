def solution():
    eligible_countries = ["UK", "Ireland", "Commonwealth"]
    john_kerry_citizen = "United States"
    election_year = 2010
    if john_kerry_citizen not in eligible_countries and election_year == 2010:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())
def solution():
    elephant_gestation_period = 95
    solar_eclipse_years = [2029]
    pregnancy_duration_in_years = elephant_gestation_period/52
    if max(solar_eclipse_years) < 2020 + pregnancy_duration_in_years:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
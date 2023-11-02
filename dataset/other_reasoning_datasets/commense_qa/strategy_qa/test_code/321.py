def solution():
    great_recession_unemployment_peak = 10
    great_depression_global_GDP_decline = 30
    great_depression_unemployment_approach = 25
    coronavirus_unemployment_may_2020 = 15
    if great_recession_unemployment_peak < great_depression_unemployment_approach and great_recession_unemployment_peak < coronavirus_unemployment_may_2020:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
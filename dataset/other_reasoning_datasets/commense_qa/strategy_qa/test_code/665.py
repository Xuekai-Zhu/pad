def solution():
    portuguese_colonial_war_countries = ["Portugal", "People's Movement for Liberation of Angola"]
    switzerland_role_in_ww2 = "neutral"
    overlap = [country for country in portuguese_colonial_war_countries if country == switzerland_role_in_ww2]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
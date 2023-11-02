def solution():
    first_tv_sale_year = 1946
    iron_chef_airs_year = 1993
    korea_japanese_rule_years = [1910, 1945]
    if iron_chef_airs_year > korea_japanese_rule_years[0] and iron_chef_airs_year < korea_japanese_rule_years[1]:
        result = "It is impossible to determine"
    else:
        result = "no"
    return result

print(solution())
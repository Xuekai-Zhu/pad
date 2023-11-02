def solution():
    airtrain_jfk_built_year = 2003
    katharine_hepburn_death_year = 2003
    katharine_hepburn_death_month = "June"
    airtrain_jfk_built_month = "December"
    if (katharine_hepburn_death_year < airtrain_jfk_built_year) or (katharine_hepburn_death_year == airtrain_jfk_built_year and katharine_hepburn_death_month < airtrain_jfk_built_month):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
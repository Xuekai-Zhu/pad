def solution():
    
    asaf_age = 50
    total_age = 140
    alexander_age = total_age - asaf_age
    pencils_asaf = (alexander_age - asaf_age) * 2
    pencils_alexander = pencils_asaf + 60
    total_pencils = pencils_asaf + pencils_alexander
    result = total_pencils
    return result

print(solution())
def solution():
    """The age difference between Asaf and Alexander's age is half the total number of pencils Asaf has. The sum of their ages is 140, and Asaf is 50 years old. If Alexander has 60 more pencils than Asaf, calculate the total number of pencils they have together."""
    asaf_age = 50
    total_age = 140
    alexander_age = total_age - asaf_age
    pencils_asaf = (alexander_age - asaf_age) * 2
    pencils_alexander = pencils_asaf + 60
    total_pencils = pencils_asaf + pencils_alexander
    result = total_pencils
    return result

print(solution())
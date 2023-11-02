def solution():
    james_age_8_years_ago = 2 * (janet_age_8_years_ago) # Since James was twice Janet's age 8 years ago
    james_age_now = james_age_8_years_ago + 8 # James' current age
    james_age_in_15_years = james_age_now + 15 # James' age in 15 years

    susan_age_diff = janet_age_8_years_ago - 3 # Age difference between Janet and Susan
    susan_age_now = susan_age_diff + 8 # Susan's current age
    susan_age_in_5_years = susan_age_now + 5 # Susan's age in 5 years

    result = susan_age_in_5_years
    return result

print(solution())
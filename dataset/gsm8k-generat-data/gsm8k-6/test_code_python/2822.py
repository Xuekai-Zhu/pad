def solution():
    # Find Jennifer's age now
    age_Jennifer_now = 30 - 10

    # Find Jordana's age when Jennifer is 30
    age_Jordana_in_10_years = age_Jennifer_now * 3

    # Find Jordana's current age
    age_Jordana_now = age_Jordana_in_10_years - 10
    result = age_Jordana_now
    return result

print(solution())
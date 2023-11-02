def solution():
    total_ducks = 40
    percent_muscovy = 50
    percent_female_muscovy = 30
    num_muscovy = total_ducks * (percent_muscovy / 100)
    num_female_muscovy = num_muscovy * (percent_female_muscovy / 100)
    result = num_female_muscovy
    return result

print(solution())
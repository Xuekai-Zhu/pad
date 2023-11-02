def solution():
    
    participants_2018 = 150
    participants_2019 = (2 * participants_2018) + 20
    participants_2020 = (participants_2019 / 2) - 40
    diff_2019_2020 = participants_2019 - participants_2020
    result = diff_2019_2020
    return result

print(solution())
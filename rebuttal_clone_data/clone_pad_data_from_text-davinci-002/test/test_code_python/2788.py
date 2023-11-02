def solution():
    participants_2018 = 150
    participants_2019 = participants_2018 * 2 + 20
    participants_2020 = participants_2019 / 2 - 40
    result = participants_2019 - participants_2020
    return result

print(solution())
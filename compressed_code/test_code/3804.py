def solution():
    
    participants_2018 = 150
    participants_2019 = 20 + 2 * participants_2018
    participants_2020 = (1/2) * participants_2019 - 40
    difference = participants_2019 - participants_2020
    result = difference
    return result

print(solution())
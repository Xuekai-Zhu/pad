def solution():
    # Calculate the number of participants in 2019 and 2020
    participants_2019 = 2 * 150 + 20  # 20 more than twice the number of participants in 2018
    participants_2020 = (1/2) * participants_2019 - 40  # 40 less than half the number of participants in 2019

    # Find the difference between the number of participants in 2019 and 2020
    difference = participants_2019 - participants_2020
    result = difference
    return result

print(solution())
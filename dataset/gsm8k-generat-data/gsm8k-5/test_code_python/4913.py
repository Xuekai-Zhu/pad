def solution():
    participants_2018 = 150
    participants_2019 = 2 * participants_2018 + 20
    participants_2020 = (participants_2019 / 2) - 40

    # Calculate the difference in participants between 2019 and 2020
    difference = participants_2019 - participants_2020
    result = difference
    return result

print(solution())
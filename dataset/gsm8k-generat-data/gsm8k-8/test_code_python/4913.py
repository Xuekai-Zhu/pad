def solution():
    # Define the number of participants in 2018
    participants_2018 = 150

    # Calculate the number of participants in 2019
    participants_2019 = 2 * participants_2018 + 20

    # Calculate the number of participants in 2020
    participants_2020 = 0.5 * participants_2019 - 40

    # Calculate the difference between the number of participants in 2019 and 2020
    difference = participants_2019 - participants_2020

    result = difference
    return result

print(solution())
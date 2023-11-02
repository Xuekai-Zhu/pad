def solution():
    num_participants_2018 = 150

    # Calculate the number of participants in 2019
    num_participants_2019 = 2*num_participants_2018 + 20

    # Calculate the number of participants in 2020
    num_participants_2020 = (num_participants_2019/2) - 40

    # Calculate the difference in participants between 2019 and 2020
    difference = num_participants_2019 - num_participants_2020
    result = difference
    return result

print(solution())
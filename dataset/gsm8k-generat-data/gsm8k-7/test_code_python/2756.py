def solution():
    num_stores_2018 = 23
    num_new_stores_2019 = 5
    num_closing_stores_2019 = 2
    num_new_stores_2020 = 10
    num_closing_stores_2020 = 6

    # Calculate the number of stores in 2019
    num_stores_2019 = num_stores_2018 + num_new_stores_2019 - num_closing_stores_2019

    # Calculate the number of stores in 2020
    num_stores_2020 = num_stores_2019 + num_new_stores_2020 - num_closing_stores_2020
    result = num_stores_2020
    return result

print(solution())
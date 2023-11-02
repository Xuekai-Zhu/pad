def solution():
    """Over the past five years, on July 4th, the high temperature for Washington, DC has been: 90 degrees in 2020, 90 degrees in 2019, 90 degrees in 2018, 79 degrees in 2017 and 71 degrees in 2016. What is the average temperature for July 4th in Washington, DC over the past 5 years?"""
    temp_2020 = 90
    temp_2019 = 90
    temp_2018 = 90
    temp_2017 = 79
    temp_2016 = 71
    total_temp = temp_2020 + temp_2019 + temp_2018 + temp_2017 + temp_2016
    average_temp = total_temp / 5
    result = average_temp
    return result

print(solution())
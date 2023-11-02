def solution():
    # Define the temperatures for each year
    temp_2020 = 90
    temp_2019 = 90
    temp_2018 = 90
    temp_2017 = 79
    temp_2016 = 71

    # Calculate the average temperature 
    average_temp = (temp_2020 + temp_2019 + temp_2018 + temp_2017 + temp_2016) / 5
    result = average_temp
    return result

print(solution())
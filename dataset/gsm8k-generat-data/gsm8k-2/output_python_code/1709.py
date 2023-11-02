def solution():
    """Over the past five years, on July 4th, the high temperature for Washington, DC has been: 90 degrees in 2020, 90 degrees in 2019, 90 degrees in 2018, 79 degrees in 2017 and 71 degrees in 2016. What is the average temperature for July 4th in Washington, DC over the past 5 years?"""
    temperatures = [90, 90, 90, 79, 71]
    average_temperature = sum(temperatures) / len(temperatures)
    result = average_temperature
    return result

print(solution())
def solution():
    """After tests in California, the total number of Coronavirus cases was recorded as 2000 positive cases on a particular day. The number of cases increased by 500 on the second day, with 50 recoveries. On the third day, the total number of new cases spiked to 1500 with 200 recoveries. What's the total number of positive cases after the third day?"""
    # Define the initial number of positive cases
    initial_cases = 2000

    # Calculate the number of positive cases on the second day
    second_day_cases = initial_cases + 500 - 50

    # Calculate the number of positive cases on the third day
    third_day_cases = second_day_cases + 1500 - 200

    result = third_day_cases
    return result

print(solution())
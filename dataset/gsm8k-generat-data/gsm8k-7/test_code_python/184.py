def solution():
    day1_cases = 2000
    day2_new_cases = 500
    day2_recoveries = 50
    day3_new_cases = 1500
    day3_recoveries = 200

    # Calculate the total number of positive cases after day 2
    day2_cases = day1_cases + day2_new_cases - day2_recoveries

    # Calculate the total number of positive cases after day 3
    day3_cases = day2_cases + day3_new_cases - day3_recoveries
    result = day3_cases
    return result

print(solution())
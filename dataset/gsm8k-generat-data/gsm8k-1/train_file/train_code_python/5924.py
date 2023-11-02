def solution():
    """It was reported that 2000 cases of Coronavirus had been confirmed in the state of New York in May 2020. There was half the number of cases in California, which had 400 more cases than the state of Texas. What's the total number of cases that had been confirmed in all of these states?"""
    cases_NY = 2000
    cases_CA = cases_NY / 2
    cases_TX = cases_CA - 400
    total_cases = cases_NY + cases_CA + cases_TX
    result = total_cases
    return result

print(solution())
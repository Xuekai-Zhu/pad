def solution():
    cases_in_NY = 2000  # The number of cases in New York
    cases_in_CA = cases_in_NY / 2  # California has half the number of cases as New York
    cases_in_TX = cases_in_CA - 400  # Texas has 400 fewer cases than California
    total_cases = cases_in_NY + cases_in_CA + cases_in_TX  # Add the cases in all three states
    result = total_cases
    return result

print(solution())
def solution():
    """It was reported that 2000 cases of Coronavirus had been confirmed in the state of New York in May 2020. There was half the number of cases in California, which had 400 more cases than the state of Texas. What's the total number of cases that had been confirmed in all of these states?"""
    # Define the number of cases in New York
    cases_ny = 2000

    # Calculate the number of cases in Texas
    cases_tx = (cases_ny - 400) / 2

    # Calculate the number of cases in California
    cases_ca = cases_tx * 2

    # Calculate the total number of cases
    total_cases = cases_ny + cases_ca + cases_tx

    # return the result
    result = total_cases
    return result

print(solution())
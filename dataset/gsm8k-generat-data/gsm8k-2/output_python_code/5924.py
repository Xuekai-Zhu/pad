def solution():
    """It was reported that 2000 cases of Coronavirus had been confirmed in the state of New York in May 2020. There was half the number of cases in California, which had 400 more cases than the state of Texas. What's the total number of cases that had been confirmed in all of these states?"""
    ny_cases = 2000
    ca_cases = ny_cases / 2
    tx_cases = ca_cases - 400
    total_cases = ny_cases + ca_cases + tx_cases
    result = total_cases
    return result

print(solution())
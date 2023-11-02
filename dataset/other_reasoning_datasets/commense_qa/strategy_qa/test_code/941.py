def solution():
    # Define the endowment of Johns Hopkins University and the debt of the MBTA
    jhu_endowment = 6.28
    mbta_debt = 9.0
    # Check if JHU's endowment can pay off the MBTA's debt
    if jhu_endowment >= mbta_debt:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
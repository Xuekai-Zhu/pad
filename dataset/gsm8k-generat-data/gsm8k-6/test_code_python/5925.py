def solution():
    # Determine the number of cases in California
    cases_California = 2000 / 2

    # Determine the number of cases in Texas
    cases_Texas = cases_California - 400

    # Calculate the total number of confirmed cases in all three states
    total_cases = 2000 + cases_California + cases_Texas
    result = total_cases
    return result

print(solution())
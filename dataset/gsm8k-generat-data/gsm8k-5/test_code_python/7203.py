def solution():
    # Calculate the number of cases each of the first 8 customers bought
    cases_first_eight = 3
    total_cases_first_eight = cases_first_eight * 8

    # Calculate the number of cases each of the next 4 customers bought
    cases_next_four = 2
    total_cases_next_four = cases_next_four * 4

    # Calculate the number of cases each of the last 8 customers bought
    cases_last_eight = 1
    total_cases_last_eight = cases_last_eight * 8

    # Calculate the total number of cases sold
    total_cases = total_cases_first_eight + total_cases_next_four + total_cases_last_eight
    result = total_cases
    return result

print(solution())
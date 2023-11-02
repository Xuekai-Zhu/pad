def solution():
    cases_april = 20
    cases_may = 30
    bottles_per_case = 20

    # Calculate the total number of cases of bottles of soda ordered
    total_cases = cases_april + cases_may

    # Calculate the total number of bottles of soda ordered
    total_bottles = total_cases * bottles_per_case
    result = total_bottles
    return result

print(solution())
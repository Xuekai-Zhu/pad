def solution():
    # Calculate the number of bottles needed for 240 days
    bottles_needed = 240 * 0.5  # Harper drinks 1/2 bottle of mineral water per day

    # Calculate the number of cases needed and the total cost
    cases_needed = bottles_needed / 24  # 24 bottles come in each case
    total_cost = cases_needed * 12  # the cost of one case is $12.00

    result = total_cost
    return result

print(solution())
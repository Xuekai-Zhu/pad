def solution():
    intl_data_cost = 3.50  # Cost of international data per day
    intl_data_days = 10  # Emmanuel will use international data for 10 days
    regular_plan_cost = 175  # Emmanuel's monthly cost for his regular plan

    # Calculate the cost of the international data
    intl_data_total_cost = intl_data_cost * intl_data_days

    # Calculate the total cost for December
    total_cost = regular_plan_cost + intl_data_total_cost
    result = total_cost
    return result

print(solution())
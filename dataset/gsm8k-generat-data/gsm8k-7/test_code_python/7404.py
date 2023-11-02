def solution():
    search_fee_first_5_days = 100
    search_fee_after_5_days = 60
    total_days = 10

    # Calculate the total search fee for the first 5 days
    total_search_fee_first_5_days = search_fee_first_5_days * 5

    # Calculate the total search fee for the remaining days
    num_remaining_days = total_days - 5
    total_search_fee_after_5_days = search_fee_after_5_days * num_remaining_days

    # Calculate the total cost of searching for 10 days
    total_cost = total_search_fee_first_5_days + total_search_fee_after_5_days
    result = total_cost
    return result

print(solution())
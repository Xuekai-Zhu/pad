def solution():
    sheets_per_ream = 500  # A bond paper ream has 500 sheets
    price_per_ream = 27  # A bond paper ream costs $27
    sheets_needed = 5000  # The office needs 5000 sheets of bond paper

    # Calculate the number of reams needed to get 5000 sheets of paper
    reams_needed = sheets_needed / sheets_per_ream

    # Calculate the total cost of buying the needed sheets of paper
    total_cost = reams_needed * price_per_ream
    result = total_cost
    return result

print(solution())
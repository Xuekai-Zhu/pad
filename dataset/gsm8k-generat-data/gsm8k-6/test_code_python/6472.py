def solution():
    # Calculate the number of shirts and pants that are either plaid or purple
    plaid_shirts = 3
    purple_pants = 5
    total_plaid_or_purple = plaid_shirts + purple_pants

    # Calculate the number of shirts and pants that are NOT plaid or purple
    total_shirts = 5
    total_pants = 24
    num_not_plaid_or_purple = (total_shirts + total_pants) - total_plaid_or_purple

    result = num_not_plaid_or_purple
    return result

print(solution())
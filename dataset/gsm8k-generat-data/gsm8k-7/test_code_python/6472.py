def solution():
    total_shirts = 5
    total_pants = 24

    plaid_shirts = 3
    purple_pants = 5

    # Calculate the number of shirts that are neither plaid nor purple
    non_plaid_non_purple_shirts = total_shirts - plaid_shirts

    # Calculate the number of pants that are neither plaid nor purple
    non_plaid_non_purple_pants = total_pants - purple_pants

    # Calculate the total number of clothing items that are neither plaid nor purple
    total_non_plaid_non_purple = non_plaid_non_purple_shirts + non_plaid_non_purple_pants
    result = total_non_plaid_non_purple
    return result

print(solution())
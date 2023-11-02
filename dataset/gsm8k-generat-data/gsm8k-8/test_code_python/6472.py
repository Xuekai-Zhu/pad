def solution():
    # Define the number of plaid shirts and purple pants
    plaid_shirts = 3
    purple_pants = 5

    # Calculate the number of shirts and pants that are either plaid or purple
    plaid_or_purple_shirts = plaid_shirts
    plaid_or_purple_pants = purple_pants

    # Calculate the number of shirts and pants that are neither plaid nor purple
    other_shirts = 5 - plaid_shirts
    other_pants = 24 - purple_pants

    # Calculate the total number of shirts and pants that are neither plaid nor purple
    neither_shirts_nor_pants = other_shirts + other_pants
    result = neither_shirts_nor_pants
    return result

print(solution())
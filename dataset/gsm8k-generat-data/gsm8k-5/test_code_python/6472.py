def solution():
    plaid_shirts = 3  # Teairra has 3 plaid shirts
    purple_pants = 5  # Teairra has 5 purple pants
    total_shirts = 5  # Teairra has 5 shirts in total
    total_pants = 24  # Teairra has 24 pants in total

    # Calculate the number of shirts that are neither plaid nor purple
    other_shirts = total_shirts - plaid_shirts

    # Calculate the number of pants that are neither plaid nor purple
    other_pants = total_pants - purple_pants

    # Calculate the total number of items that are neither plaid nor purple
    total = other_shirts + other_pants
    result = total
    return result

print(solution())
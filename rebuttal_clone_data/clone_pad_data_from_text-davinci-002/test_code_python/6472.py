def solution():
    total_shirts = 5
    total_pants = 24
    plaid_shirts = 3
    purple_pants = 5
    non_plaid_shirts = total_shirts - plaid_shirts
    non_purple_pants = total_pants - purple_pants
    non_plaid_non_purple_items = non_plaid_shirts + non_purple_pants
    result = non_plaid_non_purple_items
    return result

print(solution())
def solution():
    """Teairra has 5 shirts and 24 pairs of pants in her closet. If 3 of Teairra's shirts are plaid and 5 of Teairra's pants are purple, how many shirts and pants does Teairra has which are neither plaid nor purple?"""
    # Define the number of shirts and pants
    shirts = 5
    pants = 24

    # Define the number of plaid shirts and purple pants
    plaid_shirts = 3
    purple_pants = 5

    # Calculate the number of shirts and pants that are neither plaid nor purple
    non_plaid_shirts = shirts - plaid_shirts
    non_purple_pants = pants - purple_pants

    # Calculate the total number of items that are neither plaid nor purple
    non_plaid_purple_items = non_plaid_shirts + non_purple_pants

    # Return the result
    result = non_plaid_purple_items
    return result

print(solution())
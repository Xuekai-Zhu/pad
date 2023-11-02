def solution():
    """Teairra has 5 shirts and 24 pairs of pants in her closet. If 3 of Teairra's shirts are plaid and 5 of Teairra's pants are purple, how many shirts and pants does Teairra has which are neither plaid nor purple?"""
    # Define the number of plaid shirts and purple pants
    plaid_shirts = 3
    purple_pants = 5

    # Define the total number of shirts and pants
    total_shirts = 5
    total_pants = 24 * 2

    # Calculate the number of shirts and pants that are neither plaid nor purple
    neither_shirt_nor_pants = (total_shirts - plaid_shirts) + (total_pants - purple_pants)

    # Display the result
    result = neither_shirt_nor_pants
    return result

print(solution())
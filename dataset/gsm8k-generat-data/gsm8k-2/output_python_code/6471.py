def solution():
    """Teairra has 5 shirts and 24 pairs of pants in her closet. If 3 of Teairra's shirts are plaid and 5 of Teairra's pants are purple, how many shirts and pants does Teairra has which are neither plaid nor purple?"""
    total_shirts = 5
    total_pants = 24
    plaid_shirts = 3
    purple_pants = 5
    non_plaid_shirts = total_shirts - plaid_shirts
    non_purple_pants = total_pants - purple_pants
    neither_shirts_nor_pants = non_plaid_shirts * non_purple_pants
    result = neither_shirts_nor_pants
    return result

print(solution())
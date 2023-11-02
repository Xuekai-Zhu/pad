def solution():
    """Jefferson has 56 bananas, while Walter, his friend, has 1/4 times fewer bananas. If they decide to combine their bananas and share them equally between themselves, how many bananas does Walter get?"""
    jefferson_bananas = 56
    walter_bananas = jefferson_bananas - (1/4 * jefferson_bananas)
    total_bananas = jefferson_bananas + walter_bananas
    walter_share = total_bananas / 2
    result = walter_share
    return result

print(solution())
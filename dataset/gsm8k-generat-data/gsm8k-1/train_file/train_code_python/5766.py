def solution():
    """Jefferson has 56 bananas, while Walter, his friend, has 1/4 times fewer bananas. If they decide to combine their bananas and share them equally between themselves, how many bananas does Walter get?"""
    jefferson_bananas = 56
    walter_bananas = jefferson_bananas - (jefferson_bananas / 4)
    total_bananas = jefferson_bananas + walter_bananas
    bananas_each = total_bananas / 2
    walter_share = bananas_each
    result = walter_share
    return result

print(solution())